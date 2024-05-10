// 프로필 사진 컴포넌트
import React from 'react';

function Icon() {
    return (
        <img src={require('./robot_profile_picture.jpg')}
             alt="Icon"
             style={{
                 width: '60px',
                 height: '60px',
                 borderRadius: '45%',
                 marginRight: '5px'
             }}
        />
    );
}

export default Icon;
