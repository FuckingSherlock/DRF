import React from 'react';
import { Link } from 'react-router-dom';

const ProjectItem = ({ project }) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.id}</td>
            <td>{project.users}</td>
            <td>{project.url}</td>
            <td>
                <Link to={`/projects/${project.todo}`}>
                    {project.todo}
                </Link>
            </td>
        </tr>
    )
}

const ProjectList = ({ projects }) => {
    return (
        <table>
            <th>Name</th>
            <th>ID</th>
            <th>Users</th>
            <th>URL</th>
            <th>TODO</th>
            {projects.map((project_) => <ProjectItem project={project_} />)}
        </table>
    )
}

export default ProjectList