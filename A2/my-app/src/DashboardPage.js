import React, { useEffect, useState } from 'react'; //[1]
import { useNavigate } from 'react-router-dom';

const DashboardPage = () => {
  const [users, setUsers] = useState([]);
  const navigate = useNavigate();
  useEffect(() => {  // [2]
    // Function to fetch the latest user data from the backend
    const containerurl="https://c3-drrupgehcq-nn.a.run.app/dashboard"
    // const containerurl="http://localhost:5002/dashboard"
    const fetchUserData = () => {
      fetch(containerurl, {
        method: 'POST',
      })
        .then((response) => response.json())
        .then((data) => {
          // Update the users state variable with the latest data
          setUsers(data.users);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    };
    // Fetch the latest user data
    fetchUserData();
  }, []);
  const handleLogout = () => {
    // Set state in Firestore
    const email = sessionStorage.getItem('email');
    // Clear session storage
    sessionStorage.clear();
    const containerurl="https://c3-drrupgehcq-nn.a.run.app/set_state"  
    // const containerurl="http://localhost:5002/set_state"
    fetch(containerurl, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        // Redirect to sign-in page
        navigate('/signin',{ replace: true });
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }; //[3]
  

  return (
    <div>
      <h1>Dashboard</h1>
      <p>Email: {sessionStorage.getItem('email')}</p>
      <p>Name: {sessionStorage.getItem('name')}</p>
      <p>Location: {sessionStorage.getItem('location')}</p>
      <p>Timestamp: {sessionStorage.getItem('timestamp')}</p>
      <h2>Users online 🟢</h2>
      <ul> [3]
        {users.map((user, index) => (
          <li key={index}>{user}</li>
        ))}
      </ul>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};//[4] [5]

export default DashboardPage;

// Rferences
// [1] 	MetaOpenSource, "React," MetaOpenSource, 2023. [Online]. Available: https://react.dev/. [Accessed 04 July 2023].
// [2] 	CodingDeft.Com, "Complete Guide to useEffect Hook in React," CodingDeft.Com, 2023. [Online]. Available: https://www.codingdeft.com/posts/react-useeffect-hook/. [Accessed 04 July 2023].
// [3] 	G. Singhal, "How to Pass JSON Values into React Components," 23 huly 2020. [Online]. Available: https://www.pluralsight.com/guides/how-to-pass-json-values-into-react-components. [Accessed 04 July 2023].
// [4] 	Contact Mentor, "Session Storage in React JS with Example," Contact Mentor, 2023. [Online]. Available: https://contactmentor.com/session-storage-react-js/. [Accessed 04 July 2023].
// [5] 	W3schools, "React Forms," W3schools, [Online]. Available: https://www.w3schools.com/react/react_forms.asp. [Accessed 04 July 2023].