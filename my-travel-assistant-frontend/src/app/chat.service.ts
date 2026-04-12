import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface ChatMessage {
  id: number;
  role: 'user' | 'bot';
  text: string;
  createdAt: string;
}

export interface ChatResponse {
  answer?: string;
  response?: string;
  status?: string;
  sessionId?: string;
}

@Injectable({ providedIn: 'root' })
export class ChatService {
  private readonly baseUrl = 'http://localhost:8080/chat';

  constructor(private http: HttpClient) {}

  sendMessage(sessionId: string | null, query: string): Observable<ChatResponse> {
    return this.http.post<ChatResponse>(this.baseUrl, { sessionId, query });
  }
}
