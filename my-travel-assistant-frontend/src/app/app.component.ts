import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ChatService, ChatMessage } from './chat.service';
import { finalize } from 'rxjs/operators';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'Travel Chat';
  query = '';
  sessionId: string | null = null;
  userId: string;
  messages: ChatMessage[] = [];
  lastResponse = '';
  isLoading = false;
  errorMessage = '';

  constructor(private chatService: ChatService, private cdr: ChangeDetectorRef) {}

  ngOnInit() {
    this.initUserId();
    this.initSession();
  }

  private initUserId() {
    const storedUserId = localStorage.getItem('userId');
    if (storedUserId) {
      this.userId = storedUserId;
    } else {
      this.userId = `user-${Date.now()}-${Math.floor(Math.random() * 10000)}`;
      localStorage.setItem('userId', this.userId);
    }
  }

  private initSession() {
    this.sessionId = `sess-${Date.now()}-${Math.floor(Math.random() * 1000)}`;
  }

  private isValidChatResponse(resp: any): resp is { answer?: string; response?: string; sessionId?: string } {
    return resp && typeof resp === 'object' && (typeof resp.answer === 'string' || typeof resp.response === 'string');
  }

  copyResponse() {
    if (!this.lastResponse) {
      return;
    }

    navigator.clipboard.writeText(this.lastResponse)
      .then(() => {
        this.errorMessage = 'Response copied to clipboard.';
        setTimeout(() => (this.errorMessage = ''), 1800);
      })
      .catch(() => {
        this.errorMessage = 'Could not copy response. Please copy manually.';
      });
  }

  submitQuery() {
    const trimmed = this.query.trim();
    if (!trimmed) {
      return;
    }

    this.errorMessage = '';
    this.messages.push({
      id: this.messages.length + 1,
      role: 'user',
      text: trimmed,
      createdAt: new Date().toISOString()
    });

    this.isLoading = true;

    this.chatService.sendMessage(this.sessionId, trimmed, this.userId)
      .pipe(finalize(() => (this.isLoading = false)))
      .subscribe({
        next: (resp) => {
          console.log('sendMessage response:', resp);

          if (!this.isValidChatResponse(resp)) {
            console.error('Invalid chat response from server:', resp);
            this.errorMessage = 'Invalid response from server. Please try again.';
            this.messages.push({
              id: this.messages.length + 1,
              role: 'bot',
              text: this.errorMessage,
              createdAt: new Date().toISOString()
            });
            return;
          }

          const botText = ((resp.answer ?? resp.response) || 'No response from server').trim();
          console.log("botText:", botText);
          this.lastResponse = botText;
          this.cdr.detectChanges();
          this.messages.push({
            id: this.messages.length + 1,
            role: 'bot',
            text: botText,
            createdAt: new Date().toISOString()
          });

          if (resp.sessionId) {
            this.sessionId = resp.sessionId;
          }
        },
        error: () => {
          this.errorMessage = 'Error communicating with backend. Try again.';
          this.messages.push({
            id: this.messages.length + 1,
            role: 'bot',
            text: this.errorMessage,
            createdAt: new Date().toISOString()
          });
        }
      });

    this.query = '';
  }
}
