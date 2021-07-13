
		var new_txt = document.getElementById('new_txt')
		new_txt.addEventListener("keyup", pressKey) 
		
		function pressKey (e) {
				if (e.key == 'Enter') 
				{
					insert_task('new_txt');
				}
			}
		
	
        function insert_task(txt) 
        {
            
			var new_txt = document.getElementById(txt)
            if (new_txt.value != '')
            {	
			//Form that wraps the added task
                var task_form = document.createElement("FORM")
                task_form.id = Math.floor(Math.random() *10000)
				task_form.innerHTML = '<br>'
                var formId = task_form.id
							
			
			//Label that contains the text of the added task
                var txt = document.createElement("LABEL")
                txt.innerHTML = new_txt.value + ' '
                txt.id = Math.floor(Math.random() *10000)
				txt.className = "unstk"
				//txt.style = "underline: thin red solid; 10px;"
                var txtId = txt.id				
				
				task_form.append(txt)
                
                                               
			//Make a Marking Button that is attached to the Task_Form
				var mark_btn = document.createElement("INPUT") 
				mark_btn.type = 'button'
				mark_btn.value = 'Done'
				mark_btn.onclick = function ()
					{

					var obj  = document.getElementById(txtId)						
					if (mark_btn.value == 'Done')	
						{					
						obj.className = "stk"
						mark_btn.value = 'Reopen'
						}
					else 
						{
						obj.className = "unstk"						
						mark_btn.value = 'Done'				
						}
					}
				task_form.append(mark_btn)
				task_form.append(" ")
					
			// Make an Edit btn that is attached to the Task_Form
				var EditBtn = document.createElement("INPUT")
				EditBtn.type = 'button'
				EditBtn.value = 'Edit'
				EditBtn.onclick = function () 
					{
					var EditObj = document.getElementById(txtId)
					var txt = EditObj.innerHTML
					EditObj.setAttribute("contenteditable", Boolean(1-EditObj.isContentEditable))
					EditObj.className = 'edit'.repeat(EditObj.isContentEditable)+'unedit'.repeat(1-EditObj.isContentEditable)
					EditBtn.value = 'Edit'.repeat(1-EditObj.isContentEditable)+'Unedit'.repeat(EditObj.isContentEditable)
					}
				task_form.append(EditBtn)
				task_form.append(" ")


			//Make a Delete Button that is attached to the Task_Form
				var btn = document.createElement("INPUT")
				btn.type = 'button'
                btn.value = 'Delete'
				btn.onclick = function () 
                    {
                    var obj  = document.getElementById(formId)
					obj.remove()
                    } 				
                task_form.append(btn)
				
                document.body.append(task_form)
            }
            else {
                alert('Your new task is Empty!')
            }
			
			new_txt.value = ''
        }