# 181220 수업정리

## 1. html

- h1 헤딩은 한번 씀

- markup(markdown)의 의미는 역할 지정.

- html (hypertext 파트가 힘들다) -> 이거 자체로는 그냥 문서자체.

- 스타일시트를 이용하자.
- css만 잘해도 먹고는 산다
- 서버는 서빙해주는 역할 즉 우리는 제공자가 된다.
- 모든 프로그램은 서버를 거치는 클라이언트 프로그램
- 앱을 만든다는 것은 서버를 짠다는 것. (네트워크에 접속하기위한 과정)



## 2. def

- ### 호출과 정의는 다르다.

- 단 순서의 영향을 받는다!

- 함수 정의는 항상 위에 올려라

- 함수는 리턴하거나 혹은 아무것도 리턴안하거나

- 함수는 리턴이 대부분 되지만 메소드는 리턴이 안될 수도 있다. (문제는 리턴이 되는 안되든 작동은 된다는거)

- ```python
  a = sorted([3, 2, 1])
  def sorted():
      asdfasdfsadf
      asdfasdfsadfa
      sdfsadf
      return asdfasdf
  b = [3, 2, 1].sort()
  def sort():
      asdfasdfasdf
      asdfasdf
      asdfsadfasdf
  print(a, b)
  ```

- none 이 나왔다는 것은 return 할게 없다는 것.

- none  이 안나오면 return 값 없다

- 인자가 있고, 리턴이 있다. / yes in (괄호를 보고) yes out (return이 쓰여있는지 봐라)

- 인자가 있고, 리턴이 없다. / yes in no out

- 인자가 없고, 리턴이 있다. / no in yes out

- 인자가 없고, 리턴도 없다. / no in no out