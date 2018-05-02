//[editor Javascript]

//Project: Marlet-Admin-GIZZAL MASTER - Responsive Admin Template
//Version:  0.5B
//Last change:  20/02/2018
//Primary use:   Used only for the wysihtml5 Editor 


//Add text editor
    $(function () {
    "use strict";

    // Replace the <textarea id="editor1"> with a CKEditor
	// instance, using default configuration.
	CKEDITOR.replace('editor1')
	//bootstrap WYSIHTML5 - text editor
	$('.textarea').wysihtml5();		
	
  });

