import React from 'react';
import { useParams } from 'react-router-dom';

const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>{project.id}</td>
            <td>{project.name}</td>
            <td>{project.users}</td>
            <td>{project.url}</td>
        </tr>
    )
}

const UserProjects = ({ projects }) => {
    let { userId } = useParams()
    console.log(userId)
    let filter_projects = projects.filter((project) => project.users.includes(parseInt(userId)))
    return (
        <table>
            <th>ID</th>
            <th>Name</th>
            <th>Users</th>
            <th>URL</th>
            {filter_projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

export default UserProjects