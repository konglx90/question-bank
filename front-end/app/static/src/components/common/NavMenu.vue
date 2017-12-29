<template lang="html">
  <el-menu default-active="1" id="nav-menu" theme="dark">
    <div class="logo">
      <router-link to="/">
        <img src="../../assets/images/logo.svg" />
      </router-link>
    </div>
    <el-submenu index="1">
      <template slot="title"><i class="el-icon-menu"></i>电力系统题库</template>
      <el-menu-item index="1-1"><router-link to="/my-data" class="nav-link">我的数据</router-link></el-menu-item>
      <el-menu-item index="1-2"><router-link to="/question" class="nav-link">题库管理</router-link></el-menu-item>
      <el-menu-item index="1-3"><router-link to="/paper" class="nav-link">试卷</router-link></el-menu-item>
    </el-submenu>
  </el-menu>
</template>
