import React, { useState } from 'react'; //[1]
import { useNavigate } from 'react-router-dom';

function SignInForm() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    // Create an object with the form data
    const formData = {
      email: email,
      password: password
    };
    const containerurl="https://c2-drrupgehcq-nn.a.run.app/signin"
    // const containerurl="https://localjost:5001/signin"
    fetch(containerurl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // Check if sign-in was successful
        if (data.status === 'Success') {
          // Store user information in session storage
          sessionStorage.setItem('email', data.email);
          sessionStorage.setItem('name', data.name);
          sessionStorage.setItem('location', data.location);
          sessionStorage.setItem('timestamp', data.timestamp);
          sessionStorage.setItem('users', data.users);  //[2]
          navigate('/dashboard');
        } else {
          // Display an alert for a failed sign-in attempt
          alert('Sign-in failed. Please check your credentials.');
        }
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }; //[3]

  return (
    <div>
      <h1>Sign In</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Sign In</button>
      </form>
      <br />
      <a href="/signup">Sign up</a>
    </div>
  );
} //[4]

export default SignInForm;

// Rferences
// [1] 	MetaOpenSource, "React," MetaOpenSource, 2023. [Online]. Available: https://react.dev/. [Accessed 04 July 2023].
// [2] 	Contact Mentor, "Session Storage in React JS with Example," Contact Mentor, 2023. [Online]. Available: https://contactmentor.com/session-storage-react-js/. [Accessed 04 July 2023].
// [3] 	G. Singhal, "How to Pass JSON Values into React Components," 23 huly 2020. [Online]. Available: https://www.pluralsight.com/guides/how-to-pass-json-values-into-react-components. [Accessed 04 July 2023].
// [4] 	W3schools, "React Forms," W3schools, [Online]. Available: https://www.w3schools.com/react/react_forms.asp. [Accessed 04 July 2023].