import React from 'react';
import { Link } from 'react-router-dom';

const TodoItem = ({ todo }) => {
    return (
        <tr>
            <td>
                <Link to={`/projects/${todo.project.id}`}>
                    {todo.project.name}
                </Link>
            </td>
            <td>{todo.author}</td>
            <td>{todo.modified}</td>
            <td>{todo.is_active}</td>
            <td>{todo.text}</td>
        </tr>
    )
}

const TodoList = ({ todos }) => {

    return (
        <table>
            <th>Project</th>
            <th>Author</th>
            <th>Modified</th>
            <th>Is active</th>
            <th>Text</th>
            {todos.map((todo_) => <TodoItem todo={todo_} />)}
        </table>
    )
}

export default TodoList