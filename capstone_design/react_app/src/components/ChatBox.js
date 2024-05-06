// 채팅창 및 채팅 메시지 생성 컴포넌트
import React, { useEffect, useRef } from 'react';
import Icon from './Icon';
import Message from './Message';

function ChatBox({ history }) {
    const messageEndRef = useRef(); // 스크롤의 하단을 가리킬 객체 생성

    useEffect(() => {
        messageEndRef.current.scrollIntoView({ behavior: 'smooth' });   // 화면이 업데이트될 때마다 스크롤이 채팅 박스의 하단에 위치하도록 조작
    }, [history]);

    return (
        <div
            style={{
                margin: '10px',
                padding: '15px 25px',
                width: '80%',
                height: '70%',
                border: '1px solid transparent',
                borderRadius: '15px',
                position: 'relative',
                bottom: '1px',
                top: '1px',
                overflowY: 'auto',  // 스크롤 가능하도록 설정
                overflowAnchor: 'none', // 페이지 새로고침 시, 스크롤바가 상단에 고정돼 있지 않게 설정
                backgroundColor: 'rgba(240, 240, 240, 0.7)'
            }}
        >
            {/* 모든 메시지를 화면에 배치하는 함수 */}
            {/* 아래는 React 컴포넌트에서 JSX를 생성하는 데 사용되는 JavaScript의 배열 메서드 */}
            {history.map((message, index) => (
                <>
                    {message.role === 'consultant' && <Icon />}<Message key={index} role={message.role} content={message.content} />
                </>
            ))}
            <div ref={messageEndRef}></div>
            {/*<-- 이 위치로 스크롤이 내려오게 할 것*/}
        </div>
    );
}

export default ChatBox;
