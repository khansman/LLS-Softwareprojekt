import { Injectable } from '@angular/core';
import { ChatMessageDto } from '../models/chatMessageDto';
import { HttpClient } from '@angular/common/http';
import { Observable, of } from 'rxjs';

const messageMock: ChatMessageDto = {
  user: 'Jule',
  message: "Guten Tag!",
}


@Injectable({
  providedIn: 'root'
})

export class CommunicationService {
  url: string = 'http://localhost:8080';

  constructor(private httpClient: HttpClient) { }

  postMessage(postObject: ChatMessageDto): void {
    let url: string = `${this.url}/send`;
    this.httpClient.post<ChatMessageDto>(url, postObject);    
  }

  receiveMessage(): Observable<ChatMessageDto> {
    let url: string = `${this.url}/receive`;
    return this.httpClient.get<ChatMessageDto>(url);    
  }

  receiveMessageMock(): Observable<ChatMessageDto> {

    return of(messageMock);
  }

}
