import React, { useState, useRef, useEffect } from 'react';
import background from "./background-blurry-restaurant-shop-interior.jpg";
import './App.css';

const API_URL = "https://api-inference.huggingface.co/models/EleutherAI/polyglot-ko-1.3b";
const API_TOKEN = "___________________";
const headers = { "Authorization": `Bearer ${API_TOKEN}` };


function ChatApp() {
    // 상태 변수들을 정의
    const [history, setHistory] = useState([]); // 모든 메시지를 관리하는 상태 변수 (이전 메시지 기록)
    const [inputMessage, setInputMessage] = useState(''); // 사용자 입력을 관리하는 상태 변수 (생성된 응답 기록)
    const inputRef = useRef(); // 입력 요소를 참조하기 위한 inputRef 함수 생성 (웹페이지가 갱신될 때, 커서가 특정 요소에 자동으로 위치하게 하는 역할)
    const messageEndRef = useRef();  // 스크롤의 하단을 가리킬 객체 생성
    // 메시지 전송 핸들러 함수 (사용자 입력을 처리하고 API를 호출하는 함수)
    const handleSubmit = async (e) => {
        e.preventDefault();
        const newHistory = { role: 'user', content: inputMessage };
        setHistory([...history, newHistory]);
        setInputMessage('');

        try {
            const response = await fetch('http://fastapi_app:5000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ messages: [...history] }),    // 지난 대화 내용을 json 타입의 데이터로 변환
            });

            if (response.ok) {
                const data = await response.json();
                const consultantMessage = { role: 'consultant', content: data.result };
                setHistory([...history, consultantMessage]);

            } else {
                throw new Error('Network response was not ok');
            }
        } catch (error) {
            console.error('Error:', error);
        }
    };


    useEffect(() => {
        inputRef.current.focus();    // 화면이 업데이트될 때마다 입력 요소에 포커스 (커서가 특정 요소에 자동으로 위치하게끔 동작)
        messageEndRef.current.scrollIntoView({ behavior: 'smooth' });     // 화면이 업데이트될 때마다 스크롤이 채팅 박스의 하단에 위치하도록 조작
    }, [history]);

    // UI를 구성할 태그들을 반환
    return (
        <div style={{
            backgroundImage: `url(${background})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
            height: '100vh',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
        }}>
            <h1 style={{
                textAlign: 'center',
                margin: '10px',
                padding: '10px 30px',
                border: '1px solid transparent',
                borderRadius: '15px',
                backgroundColor: 'rgba(240, 240, 240, 0.7)'}}>🤖 학생 진로 상담 AI 챗봇 (polyglot-ko-1.3B 기반)</h1>
            <div style={{
                margin: '10px',
                padding: '15px 25px',
                width: '80%',
                height: '70%',
                border: '1px solid transparent',
                borderRadius: '15px',
                position: 'relative',
                bottom: '1px',
                top: '1px',
                overflowY: 'auto', // 스크롤 가능하도록 설정
                overflowAnchor: 'none',
                backgroundColor: 'rgba(240, 240, 240, 0.7)'
            }}>
                {/* 모든 메시지를 표시하는 반복문 */}
                {/* 아래는 React 컴포넌트에서 JSX를 생성하는 데 사용되는 JavaScript의 배열 메서드 */}
                {history.slice(0).map((message, index) => (
                    <div key={index}
                         style={{
                             display: 'flex',   // div 태그를 행 단위로 배치
                             justifyContent: message.role === 'user' ? 'flex-end' : 'flex-start', // 학생이면 행의 오른쪽, 챗봇이면 행의 왼쪽에 배치
                         }}>
                             <div
                                style={{
                                    textAlign: message.role === 'user' ? 'right' : 'left',
                                    margin: '10px',
                                    width: 'auto',  // 채팅 박스의 길이를 자동으로 조절하도록 설정
                                    maxWidth: '50%',    // 채팅 박스의 최대 너비 설정
                                    padding: '15px 25px',
                                    border: '1px solid #ccc',
                                    borderRadius: '5px',
                                    backgroundColor: message.role === 'user' ? '#e6f7ff' : '#f0f0f0'
                                 }}>
                                    <strong>{message.role === 'user' ? '학생' : 'AI 상담사'} : </strong> {message.content}

                             </div>
                    </div>
                ))}
                <div ref={messageEndRef}></div>
                {/*<-- 이 위치로 스크롤이 내려오게 할 것*/}
                {/* 입력 폼 */}
                <form onSubmit={handleSubmit} style={{
                    position: 'fixed',
                    bottom: 0,
                    left: 0,
                    width: '100%',
                    height: '10%',
                    padding: '10px',
                    backgroundColor: '#f0f0f0'
                }}>
                    <textarea
                        value={inputMessage}
                        onChange={(e) => setInputMessage(e.target.value)} //이용자가 입력창에 텍스트를 입력하거나 수정할 때마다 실시간으로 실행되는 리액트 이벤트 함수
                        placeholder="원하시는 상담 내용을 입력해주세요. 친절하게 알려드릴게요:)"
                        ref={inputRef}
                        style={{
                            width: 'calc(100% - 130px)',
                            height: '85%',
                            marginRight: '10px',
                            padding: '5px'
                        }}
                    />
                    <button type="submit" style={{
                        width: '5%',
                        padding: '20px 45px',
                        position: 'relative',
                        bottom: '25px',
                        right: '3px',
                    }}><span style={{
                        position: 'absolute',
                        left: '50%',
                        top: '50%',
                        transform: 'translate(-50%, -50%)',
                    }}>send</span>
                    </button>
                </form>
            </div>
        </div>
    );
}

// // 메시지를 표시하는 컴포넌트
// const Message = ({text, isUser}) => (
//     <div style={{margin: '10px', textAlign: isUser ? 'right' : 'left' }}>
//         {/* 사용자 메시지인 경우 "You:", 아닌 경우 "Bot:" 표시 */}
//         {isUser ? <strong>학생:</strong> : <strong>AI 상담사:</strong>} {text}
//     </div>
// );

export default ChatApp; // ChatApp 컴포넌트를 내보내기