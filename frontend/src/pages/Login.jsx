import React, { useState } from 'react'

import "../styles/login.css"

function Login() {
    const [email, setEmail] = useState('')
    const [message, setMessage] = useState('')
    const [password, setPassword] = useState('')

    async function handleSubmit(e) {
        console.log("SUBMIT FIRED")
        e.preventDefault()
        setMessage('')
        const response = await fetch('http://localhost:8000/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                password
            })
        })

        if (!response.ok) {
            setMessage('Login failed')
            return
        }

        const data = await response.json()
        console.log("LOGIN RESPONSE:", data)
        localStorage.setItem("token", data.access_token)
        console.log("TOKEN SAVED:", localStorage.getItem("token"))
    }

    return (
        <div className="login-container">
            <h1>Login</h1>
            <form onSubmit={handleSubmit}>
                <div className="login-form-group">
                    <label>Email</label><br />
                    <input
                        data-testid="input-email"
                        type="email"
                        value={email}
                        onChange={e => setEmail(e.target.value)}
                        required
                        className='login-input'
                    />
                </div>
                <div className="login-form-group">
                    <label>Password</label><br />
                    <input
                        type="password"
                        value={password}
                        onChange={e => setPassword(e.target.value)}
                        required
                        className="login-input"
                    />
                </div>
                <button data-testid="btn-submit" type="submit" className="login-button">
                    Submit
                </button>
            </form>
            {message && (
                <p className="login-message" data-testid="message">
                    {message}
                </p>
            )}
        </div>
    )
}


export default Login;