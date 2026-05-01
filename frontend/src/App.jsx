import React, { useState } from 'react'

function App() {
  const [name, setName] = useState('')
  const [email, setEmail] = useState('')
  const [message, setMessage] = useState('')

  async function handleSubmit(e) {
    e.preventDefault()
    setMessage('')

    const response = await fetch('/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email }),
    })

    if (response.ok) {
      const user = await response.json()
      setMessage(`User "${user.name}" created successfully!`)
      setName('')
      setEmail('')
    } else {
      setMessage('Failed to create user.')
    }
  }

  return (
    <div style={{ maxWidth: 400, margin: '60px auto', fontFamily: 'sans-serif' }}>
      <h1>Create User</h1>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: 12 }}>
          <label>Name</label><br />
          <input
            data-testid="input-name"
            value={name}
            onChange={e => setName(e.target.value)}
            required
            style={{ width: '100%', padding: 8 }}
          />
        </div>
        <div style={{ marginBottom: 12 }}>
          <label>Email</label><br />
          <input
            data-testid="input-email"
            type="email"
            value={email}
            onChange={e => setEmail(e.target.value)}
            required
            style={{ width: '100%', padding: 8 }}
          />
        </div>
        <button data-testid="btn-submit" type="submit" style={{ padding: '8px 20px' }}>
          Submit
        </button>
      </form>
      {message && <p data-testid="message">{message}</p>}
    </div>
  )
}

export default App
