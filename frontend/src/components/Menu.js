import React from 'react';

const MenuItem = ({ item }) => {
    return (
        <tr>
            <td>{item.user}</td>
            <td>{item.project}</td>
            <td>{item.to_do}</td>
        </tr>
    )
}

const MenuList = ({ tabs }) => {
    console.log(tabs)
    return (
        <table>
            <th>User</th>
            <th>Project</th>
            <th>What is to_do??</th>
            {tabs.map((item_) => <MenuItem item={item_} />)}
        </table>
    )
}

export default MenuList
