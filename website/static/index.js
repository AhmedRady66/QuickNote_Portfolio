function delete_note(note_id) {
    fetch('/delete-note', {  // Make a POST request to the '/delete-note' endpoint
        method: 'POST',  // Use the POST method to send data
        body: JSON.stringify({ note_id: note_id })  // Send the note ID as JSON in the request body
    }).then((_res) => {  // After the request completes
        window.location.href = "/";  // Redirect the user to the homepage ("/")
    })
}
