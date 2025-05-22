// src/app/services/auth-token.service.ts

import { Injectable } from '@angular/core';
import { environment } from '../../../environments/environment';
import * as CryptoJS from 'crypto-js';

@Injectable({
  providedIn: 'root'
})
export class AuthTokenService {
  private token: string = '';

  constructor() {
    this.generateToken();
  }

  private generateToken(): void {
    const authTokenPass = environment.authTokenPass;
    const authTokenKey = CryptoJS.enc.Base64.parse(environment.authTokenKey);
    const authTokenIv = CryptoJS.enc.Utf8.parse(environment.authTokenIv);

    this.token = CryptoJS.AES.encrypt(
      authTokenPass,
      authTokenKey,
      {
        iv: authTokenIv,
        mode: CryptoJS.mode.CBC
      }
    ).toString();
  }

  getToken(): string {
    return this.token;
  }

  getHeaders(): { [key: string]: string } {
    return {
      Authorization: `Bearer ${this.getToken()}`,
      'Content-Type': 'application/json'
    };
  }
}
