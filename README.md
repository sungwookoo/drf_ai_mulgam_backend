💡 **프로젝트명**

-   Mulgam

💡 **아키텍처**

-   사용 기술
-   Python 3.9
-   개발 환경
    -   웹 개발 환경
        -   django\_restframework
        -   python
        -   vsc **or** pycharm

💡 **기능**

1.  **로그인 / 회원가입**
    -   회원가입, 로그인
        -   실패시 , 안내문구 삽입
        -   비로그인 시 Gallery1, Gallery2 조회만 가능
        -   로그인 시 사진 올리기와 내가 올린 사진 보기 가능
    -   로그아웃 기능
2.   **Introduce**
    -   페이지 소개 글
        -   첫화면 Introduce ( 팀원 소개 및 프로젝트 소개 )
3.  **Gallery 1**
    -   기능1 (**유명 화가의 화풍을 따라하는 인공지능)**
        -   비로그인 시 로그인 페이지로 이동
    -   만들어진 그림들 보여줌
4.  **Gallery 2**
    -   기능 2 (**Neural Style Transfer)**
        -   비로그인 시 로그인페이지로 이동
    -   만들어진 그림들 보여줌
5.  **마이 페이지**
    -   내가 만든 그림들 보여줌
6.  **댓글 모달**
    -   그림 클릭 시 댓글 모달

---

**💡 와이어프레임**

**로그인 / 회원가입**

![img](https://user-images.githubusercontent.com/53362965/185866086-991dfaa2-cd63-477b-bfa2-be03bd826791.png)
![img (1)](https://user-images.githubusercontent.com/53362965/185866125-f773a0d3-6ee4-4c81-ab3d-84eeab723d17.png)


### introduce

![img (2)](https://user-images.githubusercontent.com/53362965/185866143-cb248644-2b36-40d9-9b87-9ac584dec37c.png)


### mypage / gallery1 / gallery2

![img (3)](https://user-images.githubusercontent.com/53362965/185866247-729a97e8-fe33-4d28-8426-cb57dec440bc.png)



# 🚀 DB

### user

### comment

컬럼명 타입 비고

| id | int | PK |
| --- | --- | --- |
| username | string | UK |
| password | string |   |
| join\_date | datetime |   |

### **Category**

컬럼명 타입 비고

| id | int | PK |
| --- | --- | --- |
| name | string |   |

컬럼명 타입 비고

| id | int | PK |
| --- | --- | --- |
| user\_id | int | FK |
| article\_id | int | FK |
| content | string |   |
| created\_at | datetime |   |
| updated\_at | datetime |   |

### **article**

컬럼명 타입 비고

| id | int | PK |   |
| --- | --- | --- | --- |
| user\_id | int | FK |   |
| category\_id | int | FK |   |
| title | string |   |   |
| img\_url | string |   |   |
| created\_at | datetime |   |   |
| updated\_at | datetime |   |   |

# 🚀 API

## User

### login

-   login
-   logout

### signup

-   save

## Article

### gallery1

<aside> 💡 category name 1

</aside>

-   get\_list
-   save
-   update
-   delete

### gallery2

<aside> 💡 category name 2

</aside>

-   get\_list
-   save
-   update
-   delete

### mypage

<aside> 💡 사용자가 올린 게시물 페이지

</aside>

-   get\_list
-   update
-   delete

## Comment

-   get\_comment
-   save
-   update
-   delete

[\[ 팀 구성과 역할 및 일정을 확인하려면 클릭 \]](https://www.notion.so/07-Project_Mulgam-2f47b2f8566f4272a9b58d044516c8c7)
