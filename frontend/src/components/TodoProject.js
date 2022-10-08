import React from 'react';
import { useParams } from 'react-router-dom';

const TodoItem = ({ todo }) => {
    return (

        <tr>
            <td>{todo.project}</td>
            <td>{todo.author}</td>
            <td>{todo.modified}</td>
            <td>{todo.is_active}</td>
            <td>{todo.text}</td>
        </tr>
    )
}

const TodoProject = ({ todos }) => {
    let { projectId } = useParams()
    console.log(projectId)
    let filter_todos = todos.filter((todo) => todo.projects.includes(parseInt(projectId)))
    return (
        <table>
            <th>Project</th>
            <th>Author</th>
            <th>Modified</th>
            <th>Is active</th>
            <th>Text</th>
            {filter_todos.map((todo_) => <TodoItem todo={todo_} />)}
        </table>
    )
}

export default TodoProject