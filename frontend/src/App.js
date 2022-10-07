// import logo from './logo.svg';
import './App.css';
import React from "react";
import UserList from './components/Users';
import NotFound404 from './components/NotFound404';
import ProjectList from './components/Projects';
import UserProjects from './components/UserProjects';
import TodoProject from './components/Todos';
import TodoList from './components/Todos';
import Footer from './components/Footer';
import axios from 'axios';
import { BrowserRouter, Route, Routes, Link, Navigate } from "react-router-dom"

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'tabs': [],
            'projects': [],
            'todos': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState({
                'users': response.data.results
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/').then(response => {
            this.setState({
                'projects': response.data.results
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/').then(response => {
            this.setState({
                'todos': response.data.results
            })

        }).catch(error => console.log(error))

        const tabs = [{
            'user': 'user',
            'project': 'project',
            'todo': 'todo'
        }]
        this.setState({ 'tabs': tabs })
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li>
                            <Link to='/'>Users</Link>
                        </li>
                        <li>
                            <Link to='/projects'>Projects</Link>
                        </li>
                        <li>
                            <Link to='/todos'>Todos</Link>
                        </li>
                    </nav>
                    <Routes>

                        <Route exect path='/' element={<Navigate to='/users' />} />
                        <Route path='/users'>
                            <Route index element={<UserList users={this.state.users} />} />
                            <Route path=':userId' element={<UserProjects projects={this.state.projects} />} />
                        </Route>

                        <Route path='/projects'>
                            <Route index element={<ProjectList projects={this.state.projects} />} />
                            <Route path=':projectId' element={<TodoProject todos={this.state.todos} />} />
                        </Route>
                        <Route path='/todos' element={<TodoList todos={this.state.todos} />} />
                        {/* <Route exect path='/projects' element={<ProjectList projects={this.state.projects} />} /> */}
                        <Route path='*' element={<NotFound404 />} />
                        <Route path="/projects2" element={<Navigate replace to="/projects" />} />
                    </Routes>

                </BrowserRouter>

                {/* <MenuList tabs={this.state.tabs} /> */}
                <Footer />
            </div>
        )
    }

}

export default App;
