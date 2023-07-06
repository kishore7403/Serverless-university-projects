import React, { useState } from 'react'; //[1]
import { Link, useNavigate } from 'react-router-dom';

function SignUpForm() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [location, setLocation] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    const formData = {
      name: name,
      email: email,
      password: password,
      location: location
    };
    const containerurl="https://c1-drrupgehcq-nn.a.run.app/signup" // Send the form data to the backend
    // const containerurl="https://localhost:5000/signup"
    fetch(containerurl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(formData)
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        if (data.status === 'Success') {
          navigate('/signin'); // Navigate to the sign-in form if sucessfully stored
        }
      })
      .catch((error) => {
        console.error('Error:', error); // display error in console 
      });
  }; //[2]
``
  return (
    <div>
      <h1>Sign Up</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </label>
        <br />
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
        <label>
          Location:
          <input
            type="text"
            value={location}
            onChange={(e) => setLocation(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Sign Up</button>
      </form>
      <br />
      <a href="/signin">Sign In</a>
    </div> // [3]
  );
}

export default SignUpForm;

// Rferences
// [1] 	MetaOpenSource, "React," MetaOpenSource, 2023. [Online]. Available: https://react.dev/. [Accessed 04 July 2023].
// [2] 	G. Singhal, "How to Pass JSON Values into React Components," 23 huly 2020. [Online]. Available: https://www.pluralsight.com/guides/how-to-pass-json-values-into-react-components. [Accessed 04 July 2023].
// [3] 	W3schools, "React Forms," W3schools, [Online]. Available: https://www.w3schools.com/react/react_forms.asp. [Accessed 04 July 2023].