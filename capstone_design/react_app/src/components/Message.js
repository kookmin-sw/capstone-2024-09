// Message 컴포넌트
import React from 'react';

function Message({ index, role, content }) {
    return (
        <div key={index}
             style={{
                 display: 'flex',   // div 태그를 행 단위로 배치
                 justifyContent: role === 'user' ? 'flex-end' : 'flex-start', // 학생이면 행의 오른쪽, 챗봇이면 행의 왼쪽에 배치
             }}>
            <div
                style={{
                    textAlign: role === 'user' ? 'right' : 'left',
                    margin: '10px',
                    width: 'auto',  // 채팅 박스의 길이를 자동으로 조절하도록 설정
                    maxWidth: '50%',    // 채팅 박스의 최대 너비 설정
                    wordWrap: 'break-word', // 텍스트가 최대 너비를 넘어가면 단어 단위로 줄 바꿈
                    padding: '15px 25px',
                    border: '1px solid #ccc',
                    borderRadius: '5px',
                    backgroundColor: role === 'user' ? '#e6f7ff' : '#f0f0f0'
                }}>
                <strong>{role === 'user' ? '학생' : 'AI 상담사'} : </strong> {content}
            </div>
        </div>
    );
}

export default Message;
