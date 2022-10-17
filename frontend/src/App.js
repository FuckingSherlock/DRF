// import logo from './logo.svg';
import './App.css';
import React from "react";
import UserList from './components/Users';
import NotFound404 from './components/NotFound404';
import ProjectList from './components/Projects';
import UserProjects from './components/UserProjects';
import TodoProject from './components/Todos';
import TodoList from './components/Todos';
import LoginForm from './components/Auth';
import Footer from './components/Footer';
import axios from 'axios';
import Cookies from 'universal-cookie';
import { BrowserRouter, Route, Routes, Link, Navigate } from "react-router-dom"

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'tabs': [],
            'projects': [],
            'todos': [],
            'token': [],
        }
    }

    get_token(username, password) {
        const data = { username: username, password: password }
        axios.post('http://127.0.0.1:8000/api/token/', data).then(response => {
            this.set_token(response.data['access'], username)
        }).catch(error => alert('Invalid login or password'))
    }

    set_token(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token)
        cookies.set('username', username)
        console.log(cookies);
        this.setState({ 'token': token }, () => this.load_data())
        this.setState({ 'username': username })

    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({ 'token': token }, () => this.load_data())
    }

    is_auth() {

        return !!this.state.token, this.state.username
    }

    logout() {
        this.set_token('')
        this.setState({ 'users': [] }, () => this.load_data())
        this.setState({ 'projects': [] }, () => this.load_data())
        this.setState({ 'todos': [] }, () => this.load_data())
    }

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        };

        if (this.is_auth()) {
            headers['Authorization'] = 'Bearer ' + this.state.token
        }
        return headers
    }

    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', { headers }).then(response => {
            this.setState({
                'users': response.data.results
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/', { headers }).then(response => {
            this.setState({
                'projects': response.data.results
            })
        }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todo/', { headers }).then(response => {
            this.setState({
                'todos': response.data.results
            })

        }).catch(error => console.log(error))

        // const tabs = [{
        //     'user': 'user',
        //     'project': 'project',
        //     'todo': 'todo'
        // }]
        // this.setState({ 'tabs': tabs })
    }

    componentDidMount() {
        // this.load_data()
        this.get_token_from_storage()
    }

    render() {
        return (
            <div>
                {this.is_auth() ? <div>{this.state.username}<br /><button onClick={() => this.logout()}>Logout</button></div> : <LoginForm get_token={(username, password) => this.get_token(username, password)} />}
                <BrowserRouter>
                    <nav>
                        {/* <li>
                            <Link to='/login'>Login</Link>
                        </li> */}
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

                        {/* <Route exect path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)} />} /> */}


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
