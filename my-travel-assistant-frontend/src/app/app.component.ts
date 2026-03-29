import { Component, OnInit } from '@angular/core';
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
  messages: ChatMessage[] = [];
  lastResponse = '';
  isLoading = false;
  errorMessage = '';

  constructor(private chatService: ChatService) {}

  ngOnInit() {
    this.initSession();
  }

  private initSession() {
    this.sessionId = `sess-${Date.now()}-${Math.floor(Math.random() * 1000)}`;
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

    this.chatService.sendMessage(this.sessionId, trimmed)
      .pipe(finalize(() => (this.isLoading = false)))
      .subscribe({
        next: (resp) => {
          const botText = resp.answer?.trim() || 'No response from server';
          this.lastResponse = botText;
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
