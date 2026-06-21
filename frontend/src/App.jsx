import React, { useState } from 'react'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import Landing from './pages/Landing'
import Login from './pages/Login'
import CreateUser from './pages/CreateUser'


function App() {
  return ( 
    <BrowserRouter>
        <Routes>
            <Route path='/' element={<Landing />} />
            <Route path='/login' element={<Login />} />
            <Route path='/create-user' element={<CreateUser />} />
        </Routes>
    </BrowserRouter>
  )
}

export default App
