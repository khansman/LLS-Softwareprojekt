import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, NgForm, Validators } from '@angular/forms';
import { CommunicationService } from '../services/communication.service';
import { ChatMessageDto } from 'src/app/models/chatMessageDto';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.scss']
})
export class ChatComponent implements OnInit {
  allMessages: ChatMessageDto[] = [];
  users: string[] = ['Jule','Kai'];

  user_message_Form: FormGroup;

  constructor(private communicationService: CommunicationService, private formBuilder: FormBuilder) {
    this.user_message_Form = this.formBuilder.group({
      user: [this.users[0], Validators.required],
      message: ['', Validators.required]
    })
   }


  ngOnInit(): void {
    this.getMessage()
  }

  sendMessage(){
    if(this.user_message_Form.valid)
    {
      let message = new ChatMessageDto();
      console.log(this.user_message_Form.value);
      message.user = this.user_message_Form.get('user')?.value;
      message.message = this.user_message_Form.value.message;
      console.log(message.user + ' - ' + message.message);
      this.allMessages.push(message);
      this.communicationService.postMessage(message);
    }
  }

  getMessage() {
    this.communicationService.receiveMessageMock().subscribe( result => {
      this.allMessages.push(result);

    });
  }
}
