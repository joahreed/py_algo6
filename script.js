/* 
Given a string containing space separated words
Reverse each word in the string.

If you need to, use .split to start, then try to do it without.
*/

const str1 = "hello";
const expected1 = "olleh";

const str2 = "hello world";
const expected2 = "olleh dlrow";

const str3 = "abc def ghi";
const expected3 = "cba fed ihg";

/**
 * Reverses the letters in each words in the given space separated
 * string of words. Does NOT reverse the order of the words themselves.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str Contains space separated words.
 * @returns {string} The given string with each word's letters reversed.
 */
function reverseWords(str) {
    let outstring = ""
    let temp = ""
    for (let i = 0; i < str.length; i++){
        if (str[i] == " "){
            outstring = outstring + temp + str[i]
            temp = ""
        }else {
            temp = str[i] + temp
        }

    }
    outstring = outstring + temp
    return outstring
}
/* 
  Given a string,
  return a new string with the duplicates excluded

  Bonus: Keep only the last instance of each character.
*/

const three_str1 = "abcABC";
const three_expected1 = "abcABC";

const three_str2 = "helloo";
const three_expected2 = "helo";

const three_str3 = "";
const three_expected3 = "";

const three_str4 = "aa";
const three_expected4 = "a";

// Bonus
const three_str5 = "hellool";
const three_expected5 = "heol";

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {}
