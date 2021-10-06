import React, { useState, useContext } from 'react';
import { View, StyleSheet } from 'react-native';
import { Title, Alert } from 'react-native-paper';
import FormInput from '../components/FormInput';
import FormButton from '../components/FormButton';
import {Picker} from '@react-native-picker/picker';

export default function SignupScreen({ navigation }) {
  const [email, setEmail] = useState('');
  const [emailError, setEmailError] = useState("");
  
  const [password, setPassword] = useState('');
  const [passwordError, setPasswordError] = useState("");
  
  const [passwordConfirm, setPasswordConfirm] = useState("");
  const [passwordConfirmError, setPasswordConfirmError] = useState("");

  const [language, setLanguage] = useState('');
  
  const [nickname, setNickname] = useState('');
  const [nicknameError, setNickNameError] = useState("");
  
  
  const doSignUpApi = () => {
    fetch("http://192.168.1.148/user/signup/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        nickname: nickname,
        email: email,
        password: password,
        passwordConfirm: passwordConfirm,
        language: language,
      }),
    })
      .then((resp) => resp.json())
      .then((data) => {
        Alert.alert("회원가입을 축하합니다");
      })
      .then(() => {
        navigation.navigate("SignInPage");
      })
      .catch((error) => console.log("Error"));
  };
  const doSignUp = () => {
    if (nickname == "") {
      setNickNameError("닉네임을 입력해주세요");
      return false;
    } else {
      setNickNameError("");
    }

    if (email == "") {
      setEmailError("이메일을 입력해주세요");
      return false;
    } else {
      setEmailError("");
    }

    if (password == "") {
      setPasswordError("비밀번호를 입력해주세요");
      return false;
    } else {
      setPasswordError("");
    }

    if (passwordConfirm == "") {
      setPasswordConfirmError("비밀번호 확인을 입력해주세요");
      return false;
    } else {
      setPasswordConfirmError("");
    }

    if (password !== passwordConfirm) {
      setPasswordConfirmError("비밀번호가 서로 일치 하지 않습니다.");
      return false;
    } else {
      setPasswordConfirmError("");
    }
    
    doSignUpApi();
  };
  return (
    <View style={styles.container}>
      <Title style={styles.titleText}>Register to chat</Title>
      <FormInput
        labelName='Nickname'
        value={nickname}
        error={nicknameError}
        onChangeText={userNickname => setNickname(userNickname)}
      />
      <FormInput
        labelName='Email'
        value={email}
        autoCapitalize='none'
        error={emailError}
        onChangeText={userEmail => setEmail(userEmail)}
      />
      <FormInput
        labelName='Password'
        value={password}
        secureTextEntry={true}
        error={passwordError}
        onChangeText={userPassword => setPassword(userPassword)}
      />
      <FormInput
        labelName='passwordConfirm'
        value={passwordConfirm}
        secureTextEntry={true}
        error={passwordConfirmError}
        onChangeText={userPassword => setPasswordConfirm(userPassword)}
      />
      <Picker style={styles.Picker}
        value={language}
        selectedValue={language}
        onValueChange={(val, idx) => setLanguage(val)}
        >
          <Picker.Item label="Korea" value={'KO'} />
          <Picker.Item label="USA" value={'US'} />
          <Picker.Item label="Japen" value={'JP'} />
          <Picker.Item label="China" value={'CH'} />
          <Picker.Item label="France" value={'FR'} />
      </Picker>
      <FormButton
        title='Signup'
        modeValue='contained'
        labelStyle={styles.loginButtonLabel}
        onPress={doSignUp}
      />
      <FormButton
        title='GoBack'
        modeValue='contained'
        labelStyle={styles.loginButtonLabel}
        onPress={() => navigation.goBack()}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#f5f5f5',
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center'
  },
  titleText: {
    fontSize: 24,
    marginBottom: 10
  },
  loginButtonLabel: {
    fontSize: 22
  },
  navButtonText: {
    fontSize: 18
  },
  navButton: {
    marginTop: 10
  },
  Picker:{
    height: 10,
    width: 280,
  },
  PickerContainer: {
    marginTop: 10,
    marginBottom: 10,
    alignItems: 'center',
  },
});
