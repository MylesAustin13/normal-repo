#include <iostream>
#include <string>


std::string string_times(std::string input, int iter){
  std::string format = "";
  for(int i = 0;i < iter;i++){
    format += input;
  }
  
  return format;
}
int lone_sum(int a, int b, int c){
  int sum = 0;
  if(a != b and a != c){
    sum += a;
  }
  if(b != c and b != a){
    sum += b;
  }
  if(c != b and c != a){
    sum += c;
  }
  return sum;
}
bool cigar_party(int cigars, bool is_weekend){
  if(cigars < 40){
    return false;
  }
  else if(cigars > 60 && !is_weekend){
    return false;
  }
  else{
    return true;
  }

}
int caught_speeding(int speed, bool is_birthday){
  int result;
  int lowerbound = 61;
  int upperbound = 80;
  if(is_birthday){
    lowerbound += 5;
    upperbound += 5;
  }

  if(speed < lowerbound){
    return 0;
  }
  else if(speed >= lowerbound && speed <= upperbound){
    return 1;
  }
  else{
    return 2;
  }

}
int main(){

  std::cout <<" Sum Test: a = 1,b = 2,c = 2:  " << lone_sum(1,2,2)<< std::endl;
  std::cout <<" CigarParty Test: weekend with <60 cigars:  " << cigar_party(62,true)<< std::endl;
    std::cout <<" caught_speeding test: speed 80 < x < 85 without bday: " <<  caught_speeding(82,false)<< std::endl;
    std::cout <<" caught_speeding test: speed 80 < x < 85 with bday: " <<  caught_speeding(82,true)<< std::endl;
  return 0;

}

