# 1주차: 도커(Docker) 시작하기 - 컨테이너 기초

## 1. 도커(Docker)의 등장 배경과 필요성

### 1.1 애플리케이션 배포의 어려움 🤯

개발자가 프로그램을 만들면, 이 프로그램은 특정 환경(운영체제, 라이브러리 버전 등)에서 잘 동작합니다. 하지만 다른 사람의 컴퓨터나 서버에 배포하려고 하면 "내 컴퓨터에서는 잘 됐는데..."라는 문제가 자주 발생하죠. 이는 개발 환경과 배포 환경이 다르기 때문입니다.

### 1.2 가상 머신(Virtual Machine, VM)의 한계

이런 문제를 해결하기 위해 **가상 머신(VM)**이라는 기술이 사용되었습니다. VM은 물리적인 컴퓨터 안에 또 다른 가상의 컴퓨터를 만드는 방식입니다.

- **장점:** 완전히 독립된 환경을 제공하여 개발 환경과 배배포 환경의 불일치 문제를 해결해 줍니다.
    
- **단점:** 각 VM마다 별도의 운영체제(OS)를 구동해야 하므로 **용량이 크고, 시작하는 데 시간이 오래 걸리며, 자원을 많이 소모**합니다.
    

### 1.3 도커(Docker)의 등장: 컨테이너 기술 🚢

도커는 이러한 VM의 단점을 보완하기 위해 등장했습니다. 도커는 **컨테이너**라는 개념을 사용하여 애플리케이션과 필요한 모든 환경을 패키징합니다. VM처럼 무겁게 OS 전체를 가상화하는 것이 아니라, 호스트 OS의 커널을 공유하면서 애플리케이션 실행에 필요한 부분만 격리하여 사용합니다.

- **가볍고 빠르다:** OS를 포함하지 않으므로 VM보다 훨씬 가볍고 시작 속도가 빠릅니다.
    
- **일관된 환경:** 어떤 환경에서든 동일한 컨테이너를 실행하여 "내 컴퓨터에서는 되는데..." 문제를 해결합니다.
    
- **쉬운 배포:** 개발, 테스트, 운영 환경 간 애플리케이션 이동이 매우 간편합니다.
    

## 2. 도커(Docker) 아키텍처 이해하기

도커는 다음과 같은 주요 구성 요소로 이루어져 있습니다.

### 2.1 도커 엔진(Docker Engine)

도커의 핵심이 되는 부분으로, 도커 데몬(Daemon)과 도커 클라이언트(Client)로 구성됩니다.

- **도커 데몬 (dockerd):** 백그라운드에서 실행되며 이미지 빌드, 컨테이너 실행 및 관리 등 도커의 모든 작업을 처리합니다.
    
- **도커 클라이언트 (docker):** 사용자가 명령어를 입력하여 도커 데몬과 상호작용하는 도구입니다.
    

### 2.2 도커 이미지(Docker Image) 🖼️

애플리케이션을 실행하는 데 필요한 모든 것(코드, 런타임, 시스템 도구, 라이브러리, 설정 등)을 포함하는 **읽기 전용 템플릿**입니다. 이미지는 일종의 '설계도' 또는 '청사진'과 같아서, 이 이미지로부터 여러 개의 컨테이너를 생성할 수 있습니다.

- **레이어(Layer) 구조:** 이미지는 여러 개의 읽기 전용 레이어로 구성되어 효율적인 관리와 저장 공간 절약을 가능하게 합니다.
    

### 2.3 도커 컨테이너(Docker Container) 📦

도커 이미지의 '설계도'를 바탕으로 생성된 **실제 실행 가능한 인스턴스**입니다. 이미지가 붕어빵 틀이라면, 컨테이너는 그 틀로 만들어진 붕어빵 하나하나에 비유할 수 있습니다.

- 호스트 OS와 격리되어 독립적인 실행 환경을 제공합니다.
    
- 실행, 정지, 재시작, 삭제 등 생명주기를 가집니다.
    

### 2.4 도커 레지스트리(Docker Registry)

도커 이미지를 저장하고 공유하는 공간입니다. 가장 대표적인 퍼블릭 레지스트리는 **도커 허브(Docker Hub)**입니다.

- **도커 허브(Docker Hub):** 전 세계 개발자들이 이미지를 공유하고 다운로드할 수 있는 공용 저장소입니다.
    

### 2.5 도커 아키텍처 (텍스트 기반 설명)

도커 아키텍처는 크게 세 가지 주요 구성 요소인 **Docker Client**, **Docker Host**, 그리고 **Registry**가 상호작용하는 형태입니다.

- **Docker Client (도커 클라이언트):**
    
    - 사용자가 `docker build`, `docker run`, `docker pull`과 같은 명령어를 입력하는 곳입니다.
        
    - 이 클라이언트는 사용자의 요청을 **Docker Host**의 **Docker Daemon**으로 보냅니다.
        
- **Docker Host (도커 호스트):**
    
    - 이 곳에서 도커의 핵심 구성 요소들이 실행됩니다. 가장 아래에는 **Host OS** (호스트 운영체제)가 있으며, 컨테이너들은 이 OS의 커널을 공유합니다.
        
    - **Docker Daemon (도커 데몬):** **Host OS** 위에서 백그라운드로 실행되며, **Docker Client**로부터 받은 명령을 처리합니다. 이미지 빌드, 컨테이너 실행 및 중지, 삭제 등 모든 도커 작업을 관리합니다.
        
    - **Images (이미지들):** 도커 데몬이 관리하는 이미지 저장소입니다. 각 이미지는 여러 레이어로 구성됩니다.
        
    - **Containers (컨테이너들):** 이미지로부터 생성되어 실제로 애플리케이션이 실행되는 격리된 환경입니다.
        
    - **Host OS:** 도커 데몬과 컨테이너들이 실행되는 기반 운영체제입니다. 컨테이너는 호스트 OS의 커널을 공유합니다.
        
- **Registry (레지스트리, Docker Hub):**
    
    - 도커 이미지들이 저장되고 공유되는 중앙 저장소입니다.
        
    - **Docker Host**의 **Docker Daemon**은 이곳으로부터 이미지를 **Pull (다운로드)**하거나, 로컬에서 빌드한 이미지를 이곳으로 **Push (업로드)**할 수 있습니다.
        

이 세 구성 요소는 서로 유기적으로 연결되어 컨테이너화된 애플리케이션의 개발, 배포, 실행 과정을 효율적으로 만듭니다.
    ![[도커 아키텍처.png]]
### 2.6 아키텍처와 명령어 연결: 실습을 위한 준비 🚀

지금까지 도커가 무엇이며, 어떤 주요 구성 요소들로 이루어져 있는지 살펴보았습니다. 이 개념들이 어떻게 실제 명령어로 구현되는지는 다음 섹션인 **"3.2 도커 기본 명령어 실습 (확장 버전)"**에서 직접 경험해볼 수 있습니다. 예를 들어, `docker pull`은 **Registry**에서 **Image**를 **Docker Host**로 가져오는 과정이고, `docker run`은 **Docker Host**에서 **Image**를 기반으로 **Container**를 실행하는 명령이라는 것을 기억하며 실습에 참여해 보세요. 이론과 실습을 연결하면 도커에 대한 이해가 더욱 깊어질 것입니다!
## 3. 도커(Docker) 설치 및 기본 사용법

### 3.1 도커 설치 🛠️

- **Windows / macOS:** **Docker Desktop**을 설치하는 것이 가장 편리합니다. 공식 웹사이트에서 다운로드하여 설치 마법사를 따르면 됩니다.
    
    - [Docker Desktop 다운로드 링크](https://www.docker.com/products/docker-desktop/ "null")
        
- **Linux (Ubuntu 예시):**
    
    ```
    sudo apt update
    sudo apt install docker.io
    sudo systemctl start docker
    sudo systemctl enable docker
    ```
    
    (설치 후 `sudo usermod -aG docker $USER` 명령으로 현재 사용자를 docker 그룹에 추가하고 재로그인하면 `sudo` 없이 도커 명령어를 사용할 수 있습니다.)
    

### 3.2 도커 기본 명령어 실습 (확장 버전)

이제 도커의 핵심 명령어를 직접 실행해 보면서 익혀봅시다. 각 명령어의 주요 옵션도 함께 설명합니다.

#### 3.2.1 도커 버전 확인

- 도커가 제대로 설치되었는지 확인합니다.
    
    ```
    docker --version # 도커 클라이언트 버전
    # 예시: Docker version 24.0.6, build 1a79695
    docker version   # 클라이언트 및 서버(데몬) 상세 버전 정보
    ```
    ![[도커 버전 및 Hello World.png]]

#### 3.2.2 `docker pull` (이미지 다운로드)

- 도커 허브와 같은 레지스트리에서 이미지를 다운로드합니다.
    
    ```
    docker pull [이미지 이름]:[태그]
    # 태그를 지정하지 않으면 'latest' 태그가 기본값으로 사용됩니다.
    
    # 예시 1: Nginx 최신 이미지 다운로드
    docker pull nginx:latest
    
    # 예시 2: Ubuntu 22.04 LTS 이미지 다운로드
    docker pull ubuntu:22.04
    ```
    실행 결과
    ![[docker pull 실행 후 이미지 확인.png]]
#### 3.2.3 `docker run` (컨테이너 실행)

- 이미지를 기반으로 새 컨테이너를 생성하고 실행합니다.
    
    ```
    docker run [옵션] [이미지 이름]:[태그] [실행할 명령어]
    ```
    
- **주요 옵션:**
    
    - `-p [호스트포트]:[컨테이너포트]`: 호스트의 포트를 컨테이너의 포트와 연결합니다. (예: `-p 8080:80`)
        
    - `--name [이름]`: 컨테이너에 알아보기 쉬운 이름을 부여합니다. (예: `--name my-webserver`)
        
    - `-d`: 컨테이너를 백그라운드(detached mode)에서 실행하여 터미널을 점유하지 않습니다.
        
    - `-it`: `-i`(interactive)와 `-t`(tty)를 합친 것으로, 컨테이너와 상호작용 가능한 터미널을 할당합니다. (예: `-it ubuntu bash`)
        
    - `--rm`: 컨테이너가 종료될 때 자동으로 삭제합니다. (개발 및 테스트용으로 유용)
        
    - `-v [호스트경로]:[컨테이너경로]`: 호스트의 특정 경로를 컨테이너 내부에 마운트하여 데이터를 공유합니다 (볼륨).
        
    - `--network [네트워크이름]`: 특정 도커 네트워크에 컨테이너를 연결합니다.
        
    - `-e [환경변수]=[값]`: 컨테이너 내부에 환경 변수를 설정합니다.
        
- **예시:**
    
    ```
    # 예시 1: Nginx 웹 서버 컨테이너 백그라운드 실행 및 포트 연결
    docker run -p 8080:80 --name my-nginx -d nginx
    
    # 예시 2: Ubuntu 컨테이너 실행 후 bash 셸에 접속, 종료 시 자동 삭제
    docker run --rm -it ubuntu bash
    
    # 예시 3: 로컬 웹 디렉토리를 Nginx 컨테이너에 마운트하여 서비스 (현재 디렉토리의 html 폴더 가정)
    docker run -p 8080:80 --name custom-nginx -v "$(pwd)/html:/usr/share/nginx/html" -d nginx
    ```
    ![[nginx 컨테이너 생성.png]]
	nginx 컨테이너가 잘 생성되면 웹브라우저에서 테스트 하면 아래 페이지가 나옴.
	![[컨테이너 접속 결과.png]]
--rm, -it 옵션 들어갔을때
![[rm_it옵션적용.png]]
volume 옵션 지정해서 index.html 넣어줌
![[volume옵션.png]]
![[volume 옵션 결과.png]]
#### 3.2.4 `docker ps` (컨테이너 목록 확인)

- 현재 실행 중인 컨테이너 목록을 확인합니다.
    
    ```
    docker ps [옵션]
    ```
    
- **주요 옵션:**
    
    - `-a` 또는 `--all`: 모든 컨테이너(실행 중인 것과 정지된 것 모두)를 표시합니다.
        
    - `-q` 또는 `--quiet`: 컨테이너 ID만 표시합니다.
        
    - `-s` 또는 `--size`: 컨테이너의 크기 정보를 표시합니다.
        
- **예시:**
    
    ```
    # 예시 1: 실행 중인 컨테이너만 확인
    docker ps
    
    # 예시 2: 모든 컨테이너 (실행 중이거나 정지된 것 모두) 확인
    docker ps -a
    
    # 예시 3: 모든 컨테이너의 ID만 확인 (스크립트에서 유용)
    docker ps -aq
    ```
    
![[ps결과.png]]
#### 3.2.5 `docker stop` (컨테이너 정지)

- 실행 중인 컨테이너를 정지합니다.
    
    ```
    docker stop [컨테이너 ID 또는 이름]
    ```
    
- **예시:**
    
    ```
    # 예시 1: 'my-nginx' 컨테이너 정지
    docker stop my-nginx
    
    # 예시 2: 특정 ID를 가진 컨테이너 정지
    docker stop a1b2c3d4e5f6
    
    # 예시 3: 현재 실행 중인 모든 컨테이너 정지 (주의!)
    docker stop $(docker ps -aq)
    
    # 단 컨테이너 아이디 경우 다른 컨테이너 아이디랑 겹치지 않으면 전부다 쓸 필요 없음.
    ```
    ![[docker stop start 결과.png]]

#### 3.2.6 `docker start` (컨테이너 시작)

- 정지된 컨테이너를 다시 시작합니다.
    
    ```
    docker start [컨테이너 ID 또는 이름]
    ```
    
- **예시:**
    
    ```
    # 예시 1: 'my-nginx' 컨테이너 다시 시작
    docker start my-nginx
    ```
    
![[docker stop start 결과.png]]
#### 3.2.7 `docker restart` (컨테이너 재시작)

- 실행 중이거나 정지된 컨테이너를 재시작합니다.
    
    ```
    docker restart [컨테이너 ID 또는 이름]
    ```
    
- **예시:**
    
    ```
    # 예시 1: 'my-nginx' 컨테이너 재시작
    docker restart my-nginx
    ```
    

#### 3.2.8 `docker rm` (컨테이너 삭제)

- 정지된 컨테이너를 삭제합니다. 실행 중인 컨테이너는 삭제할 수 없으므로 먼저 정지해야 합니다.
    
    ```
    docker rm [옵션] [컨테이너 ID 또는 이름]
    ```
    
- **주요 옵션:**
    
    - `-f` 또는 `--force`: 실행 중인 컨테이너도 강제로 정지시킨 후 삭제합니다. (주의해서 사용)
        
- **예시:**
    
    ```
    # 예시 1: 정지된 'my-nginx' 컨테이너 삭제
    docker rm my-nginx
    
    # 예시 2: 실행 중인 컨테이너를 강제로 정지시키고 삭제
    docker rm -f my-running-container
    
    # 예시 3: 모든 정지된 컨테이너 삭제
    docker rm $(docker ps -aq)
    ```
    ![[docker rm 결과.png]]

#### 3.2.9 `docker images` (이미지 목록 확인)

- 로컬에 다운로드되거나 빌드된 이미지 목록을 확인합니다.
    
    ```
    docker images [옵션]
    ```
    
- **주요 옵션:**
    
    - `-a` 또는 `--all`: 중간 빌드 레이어 이미지까지 포함하여 모든 이미지를 표시합니다.
        
    - `-q` 또는 `--quiet`: 이미지 ID만 표시합니다.
        
    - `--digests`: 이미지 다이제스트 정보를 표시합니다.
        
- **예시:**
    
    ```
    # 예시 1: 로컬에 있는 모든 이미지 목록 확인
    docker images
    
    # 예시 2: 이미지 ID만 표시
    docker images -q
    ```
    ![[docker images 결과.png]]

#### 3.2.10 `docker rmi` (이미지 삭제)

- 로컬에 저장된 이미지를 삭제합니다. 이미지를 사용하는 컨테이너가 있다면 먼저 컨테이너를 삭제해야 합니다.
    
    ```
    docker rmi [옵션] [이미지 ID 또는 이름]:[태그]
    ```
    
- **주요 옵션:**
    
    - `-f` 또는 `--force`: 이미지를 사용하는 컨테이너가 있어도 강제로 삭제합니다. (주의해서 사용)
        
- **예시:**
    
    ```
    # 예시 1: Nginx 이미지 삭제
    docker rmi nginx:latest
    
    # 예시 2: 사용 중인 이미지 강제 삭제 (주의!)
    docker rmi -f my-image
    ```
    ![[docker rmi 결과.png]]

#### 3.2.11 `docker logs` (컨테이너 로그 확인)

- 컨테이너의 표준 출력/오류 로그를 확인합니다.
    
    ```
    docker logs [옵션] [컨테이너 ID 또는 이름]
    ```
    
- **주요 옵션:**
    
    - `-f` 또는 `--follow`: 실시간으로 로그를 계속해서 출력합니다.
        
    - `--tail [줄 수]`: 로그의 마지막 [줄 수]만큼만 출력합니다. (예: `--tail 100`)
        
    - `-t` 또는 `--timestamps`: 로그에 타임스탬프를 함께 표시합니다.
        
- **예시:**
    
    ```
    # 예시 1: 'my-nginx' 컨테이너의 모든 로그 확인
    docker logs my-nginx
    
    # 예시 2: 'my-nginx' 컨테이너의 실시간 로그 확인
    docker logs -f my-nginx
    
    # 예시 3: 'my-nginx' 컨테이너의 마지막 50줄 로그만 확인
    docker logs --tail 50 my-nginx
    ```
    ![[docker logs 결과.png]]

#### 3.2.12 `docker exec` (실행 중인 컨테이너에 명령어 실행)

- 실행 중인 컨테이너 내부에서 명령어를 실행합니다.
    
    ```
    docker exec [옵션] [컨테이너 ID 또는 이름] [실행할 명령어]
    ```
    
- **주요 옵션:**
    
    - `-it`: 컨테이너 내부에서 상호작용 가능한 셸을 실행할 때 주로 사용합니다.
        
- **예시:**
    
    ```
    # 예시 1: 'my-nginx' 컨테이너 내부의 Nginx 웹 페이지 경로 파일 목록 확인
    docker exec my-nginx ls /usr/share/nginx/html
    
    # 예시 2: 'my-nginx' 컨테이너의 bash 셸에 접속
    docker exec -it my-nginx bash
    ```
    
![[exec결과.png]]
#### 3.2.13 `docker system prune` (불필요한 도커 리소스 정리)

- 사용되지 않는 컨테이너, 이미지, 네트워크, 볼륨 등의 도커 리소스를 정리합니다.
    
    ```
    docker system prune [옵션]
    ```
    
- **주요 옵션:**
    
    - `-a` 또는 `--all`: 사용되지 않는 모든 이미지(미사용 컨테이너가 참조하는 이미지 포함)를 정리합니다.
        
    - `--volumes`: 사용되지 않는 볼륨까지 함께 정리합니다.
        
- **예시:**
 ```
    # 예시 1: 정지된 컨테이너, 사용되지 않는 네트워크, dangling 이미지 정리
    docker system prune
    
    # 예시 2: 위 내용 + 사용되지 않는 모든 이미지 정리
    docker system prune -a
    
    # 예시 3: 위 내용 + 사용되지 않는 볼륨까지 모두 정리 (가장 강력한 정리 옵션)
    docker system prune -a --volumes
 ```
![[prune 결과.png]]
#### 3.2.14 도커 네트워크 명령어 (컨테이너 간 통신 관리)

도커 네트워크는 컨테이너 간 또는 컨테이너와 호스트 간의 통신을 가능하게 합니다.

- `docker network ls` (네트워크 목록 확인)
    
    - **설명:** 현재 도커 호스트에 존재하는 네트워크 목록을 표시합니다.
        
    - **예시:**
        
        ```
        docker network ls
        # 결과 예시:
        # NETWORK ID     NAME      DRIVER    SCOPE
        # a1b2c3d4e5f6   bridge    bridge    local
        # ...
        ```
        
- `docker network create` (네트워크 생성)
    
    - **설명:** 사용자 정의 네트워크를 생성하여 컨테이너들을 격리하거나 특정 방식으로 연결할 수 있습니다.
        
    - **주요 옵션:**
        
        - `-d` 또는 `--driver [드라이버]`: 사용할 네트워크 드라이버를 지정합니다. (`bridge`, `host`, `overlay` 등, 기본값은 `bridge`)
            
        - `--subnet [서브넷]`: 네트워크의 서브넷을 지정합니다. (예: `172.18.0.0/24`)
            
        - `--gateway [게이트웨이]`: 네트워크의 게이트웨이 IP를 지정합니다.
            
    - **예시:**
        
        ```
        # 예시 1: 'my-custom-network'라는 이름의 브릿지 네트워크 생성
        docker network create my-custom-network
        
        # 예시 2: 특정 서브넷과 게이트웨이를 가진 네트워크 생성
        docker network create --subnet 172.19.0.0/24 --gateway 172.19.0.1 my-specific-network
        ```
        
- `docker network connect` (컨테이너를 네트워크에 연결)
    
    - **설명:** 실행 중인 컨테이너를 특정 네트워크에 연결합니다. `docker run` 시 `--network` 옵션으로 처음부터 연결할 수도 있습니다.
        
    - **예시:**
        
        ```
        # 예시 1: 'my-nginx' 컨테이너를 'my-custom-network'에 연결
        docker network connect my-custom-network my-nginx
        ```
        
- `docker network disconnect` (컨테이너를 네트워크에서 분리)
    
    - **설명:** 컨테이너를 네트워크에서 분리합니다.
        
    - **예시:**
        
        ```
        # 예시 1: 'my-nginx' 컨테이너를 'my-custom-network'에서 분리
        docker network disconnect my-custom-network my-nginx
        ```
        
- `docker network rm` (네트워크 삭제)
    
    - **설명:** 사용하지 않는 네트워크를 삭제합니다. 네트워크에 연결된 컨테이너가 있다면 먼저 분리해야 합니다.
        
    - **예시:**
        
        ```
        # 예시 1: 'my-custom-network' 삭제
        docker network rm my-custom-network
        ```
### 컨테이너 두개 생성하여 동일 네트워크 지정 후 ping으로 서로 통신되는지 확인
### 첫번째 컨테이너
![[network 적용.png]]
![[해당 컨테이너에서 아이피 확인 결과.png]]
### 두번째 컨테이너
```
C:\Users\user1>docker run -p 6060:80 -d --name custom_nginx_sub --network custom_network nginx
b06eb77bdc65c3720f443990c3a9e2af171f1c94173c6245400a4e98e46cbf37

C:\Users\user1>docker exec -it b06e bash
root@b06eb77bdc65:/# hostname -i
172.19.10.3
root@b06eb77bdc65:/# apt-get update && apt-get install -y iputils-ping
Get:1 http://deb.debian.org/debian bookworm InRelease [151 kB]
Get:2 http://deb.debian.org/debian bookworm-updates InRelease [55.4 kB]
Get:3 http://deb.debian.org/debian-security bookworm-security InRelease [48.0 kB]
Get:4 http://deb.debian.org/debian bookworm/main amd64 Packages [8793 kB]
Get:5 http://deb.debian.org/debian bookworm-updates/main amd64 Packages [6924 B]
Get:6 http://deb.debian.org/debian-security bookworm-security/main amd64 Packages [277 kB]
Fetched 9331 kB in 1s (8564 kB/s)
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libcap2-bin libpam-cap
The following NEW packages will be installed:
  iputils-ping libcap2-bin libpam-cap
0 upgraded, 3 newly installed, 0 to remove and 1 not upgraded.
Need to get 96.6 kB of archives.
After this operation, 312 kB of additional disk space will be used.
Get:1 http://deb.debian.org/debian bookworm/main amd64 libcap2-bin amd64 1:2.66-4+deb12u1 [34.8 kB]
Get:2 http://deb.debian.org/debian bookworm/main amd64 iputils-ping amd64 3:20221126-1+deb12u1 [47.2 kB]
Get:3 http://deb.debian.org/debian bookworm/main amd64 libpam-cap amd64 1:2.66-4+deb12u1 [14.7 kB]
Fetched 96.6 kB in 0s (3019 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package libcap2-bin.
(Reading database ... 7582 files and directories currently installed.)
Preparing to unpack .../libcap2-bin_1%3a2.66-4+deb12u1_amd64.deb ...
Unpacking libcap2-bin (1:2.66-4+deb12u1) ...
Selecting previously unselected package iputils-ping.
Preparing to unpack .../iputils-ping_3%3a20221126-1+deb12u1_amd64.deb ...
Unpacking iputils-ping (3:20221126-1+deb12u1) ...
Selecting previously unselected package libpam-cap:amd64.
Preparing to unpack .../libpam-cap_1%3a2.66-4+deb12u1_amd64.deb ...
Unpacking libpam-cap:amd64 (1:2.66-4+deb12u1) ...
Setting up libcap2-bin (1:2.66-4+deb12u1) ...
Setting up libpam-cap:amd64 (1:2.66-4+deb12u1) ...
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 78.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Readline
debconf: (Can't locate Term/ReadLine.pm in @INC (you may need to install the Term::ReadLine module) (@INC contains: /etc/perl /usr/local/lib/x86_64-linux-gnu/perl/5.36.0 /usr/local/share/perl/5.36.0 /usr/lib/x86_64-linux-gnu/perl5/5.36 /usr/share/perl5 /usr/lib/x86_64-linux-gnu/perl-base /usr/lib/x86_64-linux-gnu/perl/5.36 /usr/share/perl/5.36 /usr/local/lib/site_perl) at /usr/share/perl5/Debconf/FrontEnd/Readline.pm line 7.)
debconf: falling back to frontend: Teletype
Setting up iputils-ping (3:20221126-1+deb12u1) ...
root@b06eb77bdc65:/# ping 172.19.10.2
PING 172.19.10.2 (172.19.10.2) 56(84) bytes of data.
64 bytes from 172.19.10.2: icmp_seq=1 ttl=64 time=0.279 ms
64 bytes from 172.19.10.2: icmp_seq=2 ttl=64 time=0.047 ms
64 bytes from 172.19.10.2: icmp_seq=3 ttl=64 time=0.046 ms
64 bytes from 172.19.10.2: icmp_seq=4 ttl=64 time=0.046 ms
64 bytes from 172.19.10.2: icmp_seq=5 ttl=64 time=0.046 ms
^C
--- 172.19.10.2 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4083ms
rtt min/avg/max/mdev = 0.046/0.092/0.279/0.093 ms
root@b06eb77bdc65:/#
```
두 컨테이너간 통신이 되는 것을 볼수 있음.
단 호스트 컴퓨터(작업중인 PC)에서는 ping으로 확인 불가.
참고로 도커 네트워크내에서는 아이피 주소가 아니더라도 도커 컨테이너명으로도 통신 가능

```
root@b06eb77bdc65:/# ping custom-nginx
PING custom-nginx (172.19.10.2) 56(84) bytes of data.
64 bytes from custom-nginx.custom_network (172.19.10.2): icmp_seq=1 ttl=64 time=0.122 ms
64 bytes from custom-nginx.custom_network (172.19.10.2): icmp_seq=2 ttl=64 time=0.080 ms
64 bytes from custom-nginx.custom_network (172.19.10.2): icmp_seq=3 ttl=64 time=0.045 ms
```

## 4. 심화 내용 (선택 사항)

### 4.1 도커 데몬(Daemon)과 클라이언트(Client)의 관계

- 사용자가 `docker run`과 같은 명령어를 입력하면, 이는 도커 클라이언트를 통해 도커 데몬에게 전달됩니다. 도커 데몬은 해당 명령을 실제로 처리하고 결과를 클라이언트에 다시 전달합니다. 이 둘은 같은 컴퓨터에 있을 수도 있고, 원격으로 연결되어 있을 수도 있습니다.
    

### 4.2 컨테이너 보안의 기본적인 이해

- 컨테이너는 격리된 환경을 제공하지만, 완벽하게 안전한 것은 아닙니다. 컨테이너 내부에서 실행되는 애플리케이션의 취약점이나 잘못된 설정은 보안 문제를 야기할 수 있습니다.
    
- **루트 권한 최소화:** 컨테이너 내부에서 `root` 권한 대신 일반 사용자 권한으로 프로세스를 실행하는 것이 좋습니다.
    
- **최소한의 이미지 사용:** 필요한 패키지만 포함된 경량 이미지를 사용하면 공격 표면(Attack Surface)을 줄일 수 있습니다.
    

## 5. 실습 문제 (Practice Problems) 🧑‍💻

다음 문제들을 직접 해결해 보면서 도커 명령어를 숙달해 보세요. 모든 실습은 터미널(명령 프롬프트 또는 PowerShell)에서 진행합니다.

### 5.1 문제 1: Ubuntu 컨테이너 실행하고 셸 접속하기

1. 공식 Ubuntu 이미지를 다운로드합니다.
    
    - `docker pull ...`
        
2. 다운로드한 Ubuntu 이미지로 컨테이너를 실행하고, 컨테이너 내부의 `bash` 셸에 접속합니다. 컨테이너 종료 시 자동으로 삭제되도록 설정합니다.
    
    - `docker run ...`
        
3. 컨테이너 내부에서 `ls -l /` 명령어를 실행하여 루트 디렉터리 내용을 확인합니다.
    
4. `exit` 명령어를 입력하여 셸에서 나온 후, 컨테이너가 자동으로 삭제되었는지 `docker ps -a` 명령어로 확인합니다.
    

### 5.2 문제 2: Apache 웹 서버 컨테이너 배포하기

1. Apache 웹 서버(`httpd`) 이미지를 다운로드합니다.
    
    - `docker pull ...`
        
2. `my-apache-server`라는 이름으로 Apache 컨테이너를 백그라운드에서 실행합니다. 호스트의 8081번 포트를 컨테이너의 80번 포트와 연결하세요.
    
    - `docker run ...`
        
3. 컨테이너가 정상적으로 실행 중인지 `docker ps` 명령어로 확인합니다.
    
4. 웹 브라우저에서 `http://localhost:8081`에 접속하여 Apache의 기본 페이지를 확인합니다.
    
5. `my-apache-server` 컨테이너의 로그를 확인해 보세요.
    
    - `docker logs ...`
        
6. `my-apache-server` 컨테이너를 정지하고 삭제합니다.
    
    - `docker stop ...`
        
    - `docker rm ...`
        

### 5.3 문제 3: 사용하지 않는 도커 리소스 정리하기

1. `docker images` 명령어를 사용하여 현재 로컬에 어떤 이미지들이 있는지 확인합니다.
    
2. `docker ps -a` 명령어를 사용하여 현재 존재하거나 정지된 컨테이너들이 있는지 확인합니다.
    
3. `docker system prune -a --volumes` 명령어를 사용하여 사용하지 않는 모든 도커 리소스(정지된 컨테이너, 사용되지 않는 이미지, 네트워크, 볼륨 등)를 정리합니다.
    
4. 정리 후 `docker images`와 `docker ps -a` 명령어로 모든 리소스가 깔끔하게 정리되었는지 다시 확인합니다.
    

## 6. 1주차 최종 목표 및 질문

이번 주에는 도커가 무엇인지, 왜 필요한지, 그리고 기본적인 컨테이너 실행 및 관리에 익숙해지는 것이 목표입니다.

- `docker pull`, `docker run`, `docker ps`, `docker stop`, `docker rm`, `docker images`, `docker rmi`, `docker logs`, `docker exec`, `docker system prune` 등 핵심 명령어를 막힘없이 사용할 수 있나요?
    
- 각 명령어의 주요 옵션들이 어떤 역할을 하는지 설명할 수 있나요?
    
- `http://localhost:8080`으로 Nginx 웹 페이지에 접속할 수 있었나요?
    
- 도커 이미지와 컨테이너의 차이점을 설명할 수 있나요?
    
- **제시된 실습 문제들을 스스로 해결할 수 있었나요?**
    

궁금한 점이 있다면 언제든지 질문해주세요!