export const palindrome = (s: string) => {
  let left = 0;
  let right = s.length - 1;

  const regex = /^[a-zA-Z]+$/;

  while (left <= right) {
    while (!regex.test(s[left])) {
      left++;
    }
    while (!regex.test(s[right])) {
      right--;
    }
    if (left >= right) {
      return true;
    }
    if (s[right].toLowerCase() !== s[left].toLowerCase()) {
      return false;
    }
    left++;
    right--;
  }
  return true;
};
