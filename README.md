# KU Smart Parking Lot System

## 프로젝트 소개

### 1. 프로젝트 목표 및 결과

#### 가. 최종 목표

- 프로젝트명 : 아두이노를 이용한 스마트 주차장 자리 안내 시스템

  - 프로젝트 설명 : 각 지의 주차장들을 통합하여 관리하고 주차장을 이용하는 고객들의 편의성을 위해 빈 자리를 안내, 예약 해주는 시스템

  - 프로젝트 선정 이유 : 백화점, 관광지, 번화가의 공영주차장 등 사람들이 많이 몰리는 곳의 주차장에서 주차 공간을 찾기 위해 여러 층을 옮겨 다니며 차로 빙빙 도는 경험을 했습니다. 이런 장소에서는 주차를 하기 위해 오랜 시간이 걸리며 많은 운전자들이 주차장 내부에서 자리를 찾기 위해 창밖을 두리번거리며 운전하기 때문에 접촉사고의 우려도 있습니다. 그래서 네트워크 통신을 위해 아두이노로 스마트 주차장 자리 안내 시스템을 네트워크 프로그래밍 프로젝트 주제로 선정하게 되었습니다.

- 주요 개발 기능

  - 주차장 빈자리 정보 수집, 데이터 처리

    - 아두이노에 초음파 거리 센서를 활용하여 각 센서가 위치한 곳에 차가 있는지 없는지 정보를 수집하여 데이터를 처리하고, 각 주차장 별 주차 되어 있는 차의 수, 현재 주차 가능한 자리를 판별합니다.

  - 주차장 안내를 위한 GUI

    - 각 고객들은 GUI를 통해 주차장의 빈 자리를 찾고 미리 예약하여 바로 주차할 수 있도록 도움을 줍니다.

#### 나. 프로젝트 결과

- 아두이노를 이용한 스마트 주차장 시스템

- 프로젝트 설명 : 각 주차장의 각 층마다 설치된 아두이노 보드를 통해 센서값을 주차장 서버가 모아주고, 주차장 서버(Local Server)에서 센서값을 계산하여 주차가능 유무를 판별, 메인 서버로 전송하여 메인 서버에서는 모든 주차장의 정보들을 통합 관리하고, Client들의 접속과 Admin의 접속을 관리합니다.

### 2. 프로젝트 개발 환경

- 하드웨어 : 아두이노 Uno 보드, 초음파 센서 5개
- OS : Windows 10 Professional x64
- Python 3.8.0 , c++ - GUI Library : PyQt5
- IDE : Pycharm community edition 19.01.03, Arduino IDE

### 3. 핵심 알고리즘

- 아두이노

  - 여섯 개의 초음파 센서로부터 센서값을 받아옴
    - Arduino관련 라이브러리 중 NewPing 라이브러리 사용
    - 0.5초 단위로 초음파 센서값 배열을 Update 해줌
    - Serial print를 사용하여 Local Server의 Client로 전송

- Local Server의 Client

  - Local Server의 Client는 아두이노로부터 Python serial 라이브러리로 센서값을 받아옴.
  - 문자열 형태로 받아온 센서 값들을 strip 해주고 list로 만들어줌
  - 해당 list를 0.5초 단위로 Local Server로 전송

- Local Server

  - 메인 서버에 접속 후 자신의 ID를 전송 (ex. 신공학관)
  - 한 주차장에는 여러 층이 있을 수 있고, 각 주차장마다의 층수가 상이하므로 client 접속을 thread로 처리하여 다중 접속구현
  - 각 client들에서 받은 센서값이 5 보다 작으면 주차 불가능, 5 이상이면 주차 가능을 판별하여 { location, Floor, 0, 1, 2, 3, 4 } 형태의 dictionary를 만듬 - 해당 dictionary를 0.5초 단위로 메인 서버에 전송

- Main Server

  - 주차장 핸들러, 클라이언트 핸들러, 관리자 핸들러 3개의 thread로 각 파트의 다중 접속처리
    - 주차장 핸들러에서는 주차장(Local Server)들의 접속을 처리하고 센서값 dictionary를 받을때마다 update하여 정보를 관리
  - 클라이언트 핸들러에서는 클라이언트의 다중 접속을 처리하고 클라이언트로부터 어떤 주차장인지의 string 과 조회인지 예약인지의 string을 받아 해당 요청을 수행
  - 관리자 핸들러에서는 관리자 접속시 실시간 주차장 정보들을 계속해서 Admin으로 보내주고 현재 접속한 Client들의 ID를 전송.
  - 현재 주차장 정보를 txt형태로 각 주차장 별로 생성하여 실시간으로 write 해줌

- Client

  - 메인서버에 접속시 자신의 ID를 임의로 생성
  - ui 의 pushButton event를 처리하여 어느 주차장의 조회, 예약 인지 string을 메인 서버에 전송
  - 메인 서버에서 받아온 dictionary를 ui로 출력

- Admin
  - ui의 testBrowser로 패스워드를 입력받아 해당 string을 메인 서버에 전송하여 메인서버는 string이 패스워드를 검증 후 결과 값을 Admin으로 전송
  - 접속 후 메인 서버로부터 계속 Receive를 하여 ui 로 출력

### 4. System Design

<img src="https://user-images.githubusercontent.com/51048267/97243487-c909d780-1839-11eb-9fd5-53d62799ad71.png" width="100%"></img>

### 5. 프로젝트 진행에 따른 문제점 및 개선 방안

#### 가. 문제점

- 모든 다중접속을 Multi
- Thread를 사용하여 성능 하락
- parkinglot, admin, client 세 개의 thread 사용
- 각 주차장에서 실시간 정보를 받아오고 admin 과 client들의 request도 처리 - Client 약 50개 접속시 부하가 발생
- 주차장들의 자료구조를 미리 정해놓아서 확장성이 부족함
- singong, sanhak, haebong, gongdae 4개의 자료구조를 미리 정해놓음 - 새로운 주차장 도입시 (ex. 새천년관) 새로운 자료구조를 생성해줘야함

#### 나. 개선방안

- Multi-Process 와 Multi-thread를 적절히 사용
- 큰 세 개의 핸들러 (parkinglot, admin, client)는 멀티 프로세스로 관리하고 해당 프로세스 내에서는 멀티 쓰레드로 처리하면 부하를 줄일수 있음
- 자료구조에 대한 list 생성
- 새로운 주차장이 도입될때마다 list에 해당 주차장 ID 에대한 자료구조를 append 해줌
- 각 주차장의 정보를 사용시 list에 index로 접근하여 정보를 받아올 수 있음
