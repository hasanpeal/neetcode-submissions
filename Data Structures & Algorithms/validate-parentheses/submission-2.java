class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        HashMap <Character, Character> map = new HashMap<>();

        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');

        for(int i = 0; i < s.length(); i++){
          char currChar = s.charAt(i);
          if(currChar == '(' || currChar == '{' || currChar == '[' || currChar == ')'
          || currChar == '}' || currChar == ']'){
            if(!stack.empty()) {
              if(stack.peek() == map.get(currChar)) stack.pop();
              else stack.push(currChar);
            } else stack.push(currChar);
          }
        }
        return stack.empty() ? true: false;
    }
}
