// MessageInput 컴포넌트
import React, { useRef, useEffect } from 'react';

function MessageInput({ onSubmit, inputMessage, setInputMessage, siren }) {
    const inputRef = useRef();  // 입력 요소를 참조하기 위한 inputRef 함수 생성 (웹페이지가 갱신될 때, 커서가 특정 요소에 자동으로 위치하게 하는 역할)

    useEffect(() => {
        inputRef.current.focus();   // 화면이 업데이트될 때마다 입력 요소에 포커스 (커서가 특정 요소에 자동으로 위치하게끔 동작)
    }, [siren]);

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit();
    };

    return (
        <form
            onSubmit={handleSubmit}
            style={{
                position: 'fixed',
                bottom: 0,
                left: 0,
                width: '100%',
                height: '10%',
                padding: '10px',
                backgroundColor: '#f0f0f0'
            }}
        >
            <textarea
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="원하시는 상담 내용을 입력해주세요. 친절하게 알려드릴게요:)"
                ref={inputRef}
                style={{
                    width: 'calc(100% - 130px)',
                    height: '85%',
                    marginRight: '10px',
                    padding: '5px'
                }}
            />
            <button
                type="submit"
                style={{
                    width: '5%',
                    padding: '20px 45px',
                    position: 'relative',
                    bottom: '25px',
                    right: '3px',
                }}
            >
                <span style={{ position: 'absolute', left: '50%', top: '50%', transform: 'translate(-50%, -50%)' }}>send</span>
            </button>
        </form>
    );
}

export default MessageInput;
