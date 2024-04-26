import React, { useState, useRef, useEffect } from 'react';
import background from "./background-blurry-restaurant-shop-interior.jpg";
import './App.css';

const API_URL = "https://api-inference.huggingface.co/models/EleutherAI/polyglot-ko-1.3b";
const API_TOKEN = "___________________";
const headers = { "Authorization": `Bearer ${API_TOKEN}` };

function ChatApp() {
    // 상태 변수들을 정의
    const [messages, setMessages] = useState([]); // 모든 메시지를 관리하는 상태 변수 (이전 메시지 기록)
    const [inputText, setInputText] = useState(''); // 사용자 입력을 관리하는 상태 변수 (생성된 응답 기록)
    const inputRef = useRef(); // 입력 요소를 참조하기 위한 inputRef 함수 생성

    // 메시지 전송 핸들러 함수 (사용자 입력을 처리하고 API를 호출하는 함수)
    const handleSubmit = async (e) => {
        e.preventDefault(); // 해당 태그의 기본 동작 방지(화면 새로고침 방지)
        if (!inputText) return; // 입력이 비어있다면 아무것도 하지 않음

        try {
            // API에 POST 요청을 보내고 응답 수신
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    headers,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: inputText }) // 입력을 JSON 형식으로 변환하여 전송
            });

            if (!response.ok) { // 응답이 성공적이지 않을 경우 오류 처리
                throw new Error('Network response was not ok');
            }

            // JSON 형식으로 응답을 파싱
            const responseData = await response.json();
            const generatedText = responseData.generated_text;  // 생성형 ai로부터 반환된 응답 텍스트 저장

            // 새로운 메시지를 추가하고 입력 창을 비우는 작업 (상태 변수들을 업데이트)
            setMessages([messages, { text: inputText, isUser: true }, { text: generatedText, isUser: false }]);  // 사용자의 메시지와 ai로부터 응답받은 메시지를 기록
            setInputText(''); // 사용자의 입력 메시지를 빈 값으로 초기화
        } catch (error) { // // 오류가 발생했을 경우 콘솔창에 오류 메시지를 출력
            console.error('An error occurred:', error);
        }
    };

    // 화면이 업데이트될 때마다 입력 요소를 포커스
    useEffect(() => {
        inputRef.current.focus();
    });

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
            <h1 style={{ textAlign: 'center' }}>🤖 학생 진로 상담 AI 챗봇 (polyglot-ko-1.3B 기반)</h1>
            <div>
                {/* 모든 메시지를 표시하는 반복문 */}
                {messages.map((message, index) => (
                    <div key={index} style={{ textAlign: message.isUser ? 'right' : 'left' }}>
                        <strong>{message.isUser ? 'You' : 'Bot'}:</strong> {message.text}
                    </div>
                ))}
                {/* 입력 폼 */}
                <form onSubmit={handleSubmit} style={{ position: 'fixed', bottom: 0, left: 0, width: '100%', padding: '10px', backgroundColor: '#f0f0f0' }}>
                    <input
                        type="text"
                        value={inputText}
                        onChange={(e) => setInputText(e.target.value)}
                        placeholder="Type your message..."
                        ref={inputRef}
                        style={{ width: 'calc(100% - 120px)', marginRight: '10px', padding: '5px' }}
                    />
                    <button type="submit" style={{ padding: '5px 10px' }}>Send</button>
                </form>
            </div>
        </div>
    );
}

// 메시지를 표시하는 컴포넌트
const Message = ({ text, isUser }) => (
    <div style={{ margin: '10px', textAlign: isUser ? 'right' : 'left' }}>
        {/* 사용자 메시지인 경우 "You:", 아닌 경우 "Bot:" 표시 */}
        {isUser ? <strong>학생:</strong> : <strong>AI 상담사:</strong>} {text}
    </div>
);

export default ChatApp; // ChatApp 컴포넌트를 내보내기