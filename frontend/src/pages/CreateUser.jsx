import { useState } from "react"
import "../styles/create-user.css"

function CreateUser() {

    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const handleSubmit = async (e) => {
        e.preventDefault()
        const reponse = await fetch('http://localhost:8000/users/', {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name,
                email,
                password
            })
        })
        const data = await Response.json()
        console.log('User created', data)
    }

    return (
        <div className="create-user-container" onSubmit={handleSubmit}>
            <h1>Create User</h1>
            <form className="create-user-form">
                <input className="create-user-input"
                    placeholder='Name'
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
                <input className="create-user-input"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input className="create-user-input"
                    placeholder="Password"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)} />
                <button
                    className="create-user-button"
                    type="submit">
                    Create User
                </button>
            </form>
        </div>
    )
}

export default CreateUser;