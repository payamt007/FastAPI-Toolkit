"use client"
import React, {useState, useEffect} from 'react';
import {Button, Checkbox, Form, type FormProps, Input} from 'antd';
import {useGetTokenQuery, getTokenResponse} from "@/lib/features/auth/authApiSlice";

type FieldType = {
    username?: string;
    password?: string;
};

const onFinishFailed: FormProps<FieldType>["onFinishFailed"] = (errorInfo) => {
    console.log('Failed:', errorInfo);
};


export default function App() {
    const [token, setToken] = useState<getTokenResponse>();
    const [formValues, setFormValues] = useState<FieldType>({});

    const {data, isError, isLoading, isSuccess, refetch} =
        useGetTokenQuery(formValues, {skip: Object.keys(formValues).length === 0});

    const onFinish: FormProps<FieldType>["onFinish"] = (values) => {
        // console.log('Success:', values);
        setFormValues(values);
        refetch();
    }

    useEffect(() => {
        if (isSuccess && data) {
            setToken(data);
            // console.log(token.access_token)
        }
    }, [isSuccess, data]);


    return (
        <>
            <div>{token?.access_token}</div>
            <Form
                name="basic"
                labelCol={{span: 8}}
                wrapperCol={{span: 16}}
                style={{maxWidth: 600}}
                initialValues={{remember: true}}
                onFinish={onFinish}
                onFinishFailed={onFinishFailed}
                autoComplete="off"
            >
                <Form.Item<FieldType>
                    label="Username"
                    name="username"
                    rules={[{required: true, message: 'Please input your username!'}]}
                >
                    <Input/>
                </Form.Item>

                <Form.Item<FieldType>
                    label="Password"
                    name="password"
                    rules={[{required: true, message: 'Please input your password!'}]}
                >
                    <Input.Password/>
                </Form.Item>

                {/*<Form.Item<FieldType>*/}
                {/*    name="remember"*/}
                {/*    valuePropName="checked"*/}
                {/*    wrapperCol={{offset: 8, span: 16}}*/}
                {/*>*/}
                {/*    <Checkbox>Remember me</Checkbox>*/}
                {/*</Form.Item>*/}

                <Form.Item wrapperCol={{offset: 8, span: 16}}>
                    <Button type="primary" htmlType="submit">
                        Submit
                    </Button>
                </Form.Item>
            </Form>
        </>
    )

}
