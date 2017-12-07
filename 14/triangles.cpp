#include <iostream>
#include <string>
using std::cout;
using std::endl;
using std::string;
std::string line(int l, std::string c){
  std::string res = "";
  for(int i = 0;i < l;i++){
    res += c;

  }
  // res += "\n";
  return res;
}

std::string rect(int w, int h) {
  std::string rectangle = "";
  for(int i = 0;i<h;i++){
    rectangle += line(w,"*");
    rectangle += "\n";
  }
  return rectangle;
}

/*
 *
 **
 ***
 ****
 */
std::string tri1(int h) {
  std::string tri = "";
  int amount = 1;
  for(int i = 0; i < h;i++){
    tri += line(amount,"*");
    amount += 1;
    tri += "\n";
  }
  return tri;
}


/*
   *
  ***
 *****
 */
std::string tri2(int h) {
  std::string tri = "";
  int amount = 1;
  int max_size = (2 * h) - 1;
  int current_space = 0;
  for(int i = 0;i < h;i++){
    current_space = max_size - amount;
    
    tri += line(current_space/2," ");
    tri += line(amount,"*");
    tri += line(current_space/2," ");
    tri += "\n";
    amount += 2;

  }
  return tri;
}

/*
  *
 **
***
 */
std::string tri3(int h) {

  std::string tri = "";
  int amount = 1;
  int max_space_size = h;
  int current_space_size;
  for(int i = 0; i < h;i++){
    current_space_size = max_space_size - amount;
    tri += line(current_space_size," ");
    tri += line(amount,"*");
    amount += 1;
    tri += "\n";
  }
  return tri;
}
int main(){
  string s1 = rect(5,7);
  string s2 = tri1(5);
  string s3 = tri2(5);
  string s4 = tri3(5);
  cout<<s1<<endl;
  cout<<s2<<endl;
  cout<<s3<<endl;
  cout<<s4<<endl;
}

