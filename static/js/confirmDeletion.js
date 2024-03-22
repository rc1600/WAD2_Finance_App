// This script is used to confirm the deletion of a field (budget or financial account) before submitting the form.

function confirmDeletion(event, message) {
    event.preventDefault(); // Prevent form from submitting immediately.
    if (confirm(message)) {
        // Submit the form if the user confirms deletion
        event.target.form.submit();
    } else {
        console.log("Deletion cancelled."); // Log cancellation for debugging.
    }
}


