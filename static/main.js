function uploadToGcp() {
    const inp = document.querySelector('#file');
    if (inp.files.length == 0 || inp.files.length > 1) {
        alert('Select one file');
        return;
    }

    fetch('/get-signed-url', {
        method: 'POST',
        body: JSON.stringify({
            fname: inp.files[0].name,
            mimetype: inp.files[0].type
        }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(resp => resp.json())
    .then(data => {
        fetch(data.url, {
            method: 'PUT',
            body: inp.files[0],
            headers: {
                'Content-Type': inp.files[0].type
            }
        })
        .then(resp => {
            if (resp.ok) {
                alert('File uploaded');
            }
        })
    })

}