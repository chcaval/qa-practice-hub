import '../styles/landing.css'

export default function Landing() {
  return (
    <div className="landing-container">
      <h1>QA Practice Hub</h1>

      <p>
        Full-stack project with React + FastAPI + MongoDB + QA automation.
      </p>

      <button onClick={() => window.location.href='/create-user'}>
        Get Started
      </button>
    </div>
  )
}