// import logo from './logo.svg';
import './App.css';
import React from "react";
import UserList from './components/User';
import MenuList from './components/Menu';
import Footer from './components/Footer';
import axios from 'axios';


class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'tabs': [],
        }
    }

    componentDidMount() {
        axios.get('http://127.0.0.1:8000/api/users/').then(response => {
            this.setState({
                'users': response.data
            })
        }).catch(error => console.log(error))

        const tabs = [{
            'user': 'user',
            'project': 'project',
            'to_do': 'to_do'
        }]
        this.setState({ 'tabs': tabs })
    }

    render() {
        return (
            <div>
                <MenuList tabs={this.state.tabs} />
                <UserList users={this.state.users} />
                <Footer />
            </div>
        )
    }

}

export default App;
