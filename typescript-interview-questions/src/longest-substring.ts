export const longestSubstring = (s: string) => {
  if (s.length < 2) return s;
  let left = 0;
  const set = new Set(s[0]);
  let result = s[0];
  for (let right = 1; right < s.length; right++) {
    while (set.has(s[right])) {
      set.delete(s[left]);
      left++;
    }
    set.add(s[right]);
    if (right + 1 - left > result.length) {
      result = s.slice(left, right + 1);
    }
  }
  return result;
};
