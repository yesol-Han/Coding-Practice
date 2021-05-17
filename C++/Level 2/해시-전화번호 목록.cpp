// 2차 시도 - 정답
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    int length = phone_book.size();
    
    sort(phone_book.begin(),phone_book.end());
    
    for (int i=0; i<length-1 ; i++){
        if(phone_book[i] == phone_book[i+1].substr(0,phone_book[i].size()))
            return answer=false;
    }
    
    return answer;
}


///////////////////////////////////////////////////

// 1차 시도- 효율성 3,4 불통

#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    int length = phone_book.size();
    int comp=0;
    sort(phone_book.begin(),phone_book.end());
    
    for (int i=0; i<length ; i++){
        comp=phone_book[i].size();
        for(int j=i; j<length ; j++){
            if(i==j) continue;
            if(phone_book[i][0] != phone_book[j][0]) break;
            
            if(comp < phone_book[j].size() & phone_book[j].find(phone_book[i]) == 0){
                answer = false;
                return answer;
            }
        }
    }
    
    return answer;
}

/*
채점 결과
정확성: 83.3
효율성: 8.3
합계: 91.7 / 100.0
*/
