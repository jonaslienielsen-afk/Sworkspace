import { test } from 'node:test';
import assert from 'node:assert/strict';
import { normalize, confusableKey, parseList, buildIndex, check, extractCandidates, editDistance } from '../src/matcher.js';

test('normalize strips spacing and punctuation', () => {
  assert.equal(normalize(' ab-12 34 '), 'AB1234');
});

test('confusableKey folds look-alike characters', () => {
  assert.equal(confusableKey('O1I5'), confusableKey('0115'));
});

test('parseList: plain one-per-line list', () => {
  const r = parseList('12345678\n  23456789 \n\n34567890\n');
  assert.equal(r.rows.length, 3);
  assert.equal(r.hasHeader, false);
  assert.equal(r.serialCol, 0);
});

test('parseList: CSV with header finds serial column', () => {
  const r = parseList('Brand;Model;Serienummer;Owner\nFischer;Speedmax;20123456;"Hansen, Ola"\nMadshus;Redline;M778899;Kari');
  assert.equal(r.hasHeader, true);
  assert.equal(r.serialCol, 2);
  assert.equal(r.rows[0][3], 'Hansen, Ola');
});

test('parseList: CSV without header guesses serial column', () => {
  const r = parseList('Fischer,20123456\nAtomic,20999888\nFischer,20111222');
  assert.equal(r.hasHeader, false);
  assert.equal(r.serialCol, 1);
});

test('check: exact, look-alike, near and missing', () => {
  const { rows, serialCol } = parseList('Serial,Model\n20-123-456,Speedmax\nAB1050,Redline');
  const idx = buildIndex(rows, serialCol);
  assert.equal(check(idx, '20123456').status, 'found');
  assert.equal(check(idx, '20 123 456').status, 'found');
  assert.equal(check(idx, 'ab1o5o').status, 'possible');
  assert.equal(check(idx, '20123457').status, 'possible');
  assert.equal(check(idx, '99999999').status, 'not_found');
  assert.equal(check(idx, '').status, 'empty');
});

test('editDistance', () => {
  assert.equal(editDistance('KITTEN', 'SITTING'), 3);
  assert.equal(editDistance('ABCDEF', 'ABCDEF', 1), 0);
  assert.ok(editDistance('AAAAAA', 'BBBBBB', 1) > 1);
});

test('extractCandidates prefers listed serials and digit-heavy tokens', () => {
  const idx = buildIndex([['20123456']], 0);
  const c = extractCandidates('FISCHER SPEEDMAX\nSN 20 123 456\nMADE IN AUSTRIA', idx);
  assert.equal(c[0], '20123456');
  assert.ok(!c.includes('FISCHER'));
});
