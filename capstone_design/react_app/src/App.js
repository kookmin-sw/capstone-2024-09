// App 컴포넌트
import React, { useState } from 'react';
import background from "./background-blurry-restaurant-shop-interior.jpg";
import './App.css';
import ChatBox from './components/ChatBox';
import MessageInput from './components/MessageInput';
import LoadingSpinner from './components/LoadingSpinner';

function App() {
    // 상태 변수들을 정의
    const [history, setHistory] = useState([]); // 모든 메시지를 관리하는 상태 변수 (이전 메시지 기록)
    const [inputMessage, setInputMessage] = useState('');   // 사용자 입력을 관리하는 상태 변수 (생성된 응답 기록)
    const [loading, setLoading] = useState(false);   // 생성형 ai로부터 응답을 기다리고 있는지의 여부를 나타내는 상태 변수

    // 메시지 전송 핸들러 함수 (사용자 입력을 처리하고 API를 호출하는 함수)
    const handleSubmit = async () => {
        const newHistory = { role: 'user', content: inputMessage };

        // 로딩 상태 활성화
        setLoading(true);

        try {
            const response = await fetch('http://develop.sung4854.com:5000/api/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ messages: newHistory }),
            });

            if (response.ok) {
                const data = await response.json();
                const consultantMessage = { role: 'consultant', content: data.response };
                setHistory([...history, newHistory, consultantMessage]); // consultMessage도 함께 추가
            } else {
                throw new Error('Network response was not ok');
            }
        } catch (error) {
            console.error('Error:', error);
        } finally {
            setLoading(false); // 응답을 받은 후에 로딩 상태 해제
        }
        setInputMessage('');
    };

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
                backgroundColor: 'rgba(240, 240, 240, 0.7)'
            }}>🤖 학생 진로 상담 AI 챗봇 올빼미 🤖
                <br/>
                <small><small><small>AI 상담사와의 대화 내용을 토대로 직업을 추천받고 싶으시면 "이제 직업을 추천해주세요"라고 얘기해주세요.</small></small></small>
            </h1>
            {loading && <LoadingSpinner />} {/* 로딩 바 표시 */}
            <ChatBox history={history} />
            {/* 입력 폼 */}
            <MessageInput
                onSubmit={handleSubmit}
                inputMessage={inputMessage}
                setInputMessage={setInputMessage}
                siren={history}
            />
        </div>
    );
}

export default App;
