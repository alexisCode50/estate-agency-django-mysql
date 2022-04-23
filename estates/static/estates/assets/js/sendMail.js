function contactAdviser(event) {
	event.preventDefault()

	const form = document.getElementById('form-contact-adviser')
	const data = new FormData(form)

	fetch('/properties/contact/adviser', {
		method: 'POST',
		body: data,
	})
	.then(res => res.json())
	.then(data => {
		if (data.ok) {

			$('#nombre').val('')
			$('#email').val('')
			$('#comentarios').val('')

			toastr.success(data.mensaje)
			
		} else {
			toastr.error('Ocurrio un error al enviar el mensaje, intentalo de nuevo')
		}
	})
	.catch(err => {
		toastr.error('Ocurrio un error al enviar el mensaje, intentalo de nuevo')
	})
}