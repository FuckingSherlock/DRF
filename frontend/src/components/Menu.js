import React from 'react';

const MenuItem = ({ item }) => {
    return (
        <tr>
            <td>{item.user}</td>
            <td>{item.project}</td>
            <td>{item.todo}</td>
        </tr>
    )
}

const MenuList = ({ tabs }) => {
    console.log(tabs)
    return (
        <table>
            <th>User</th>
            <th>Project</th>
            <th>TODO</th>
            {tabs.map((item_) => <MenuItem item={item_} />)}
        </table>
    )
}

export default MenuList
