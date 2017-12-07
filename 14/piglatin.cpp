#include <iostream>
#include <string>
#include <locale>

std::string latin(std::string s){
  std::locale l;
  std::string start;
  for(int i = 0;i < s.length();i++){

    start += std::tolower(s[i]);
    //  std::cout << start << "\n";
  }
  
  std::string format = "";
  if(start[0] == 'a' || start[0] == 'e' ||start[0] == 'i'||start[0] == 'o'||start[0] == 'u'){
    format += start;
    format += "ay";

  }
  else{
    format += start.substr(1);
    format += start[0];
    format += "ay";
  }
  return format;
}

int main(){
  std::string s = latin("TEST");
  std::string s2 = latin("apple");
  std::cout << s << std::endl;
  std::cout << s2 <<std::endl;
  return 0;
}
