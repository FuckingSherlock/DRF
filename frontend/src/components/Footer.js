import React from 'react';

const Footer = () => {

    const divStyle = {
        background: 'black',
        height: '50px',
        width: '100%',
        position: 'absolute',
        bottom: 0,
        left: 0,
        color: 'white'
    };

    return (
        <div style={divStyle}>BOTTOM</div>
    )
}

export default Footer